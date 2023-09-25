from datetime import *
import random
import shlex
import string
import unicodedata
import sys
import subprocess
import os
import readline  # don't remove this, this is for input()

T = '    '  # four space tab
TT = T + T  # two tabs


def assert_true(flag: bool, msg: str = 'Illegal Argument', hint: str = None) -> None:
    """Assert the given flag is true, else print an error msg and exit the program"""
    if flag is not True:
        s = f"[Error] {msg}"
        if hint is not None:
            s += f" hint: {hint}"
        print(s)
        sys.exit(1)


def to_camel_case(s: str) -> str:
    """
    Convert a string to camel case
    """
    is_prev_uc = False  # is prev in uppercase
    s = s.lower()
    ccs = ''
    for i in range(len(s)):
        ci = s[i]
        if ci == '_':
            is_prev_uc = True
        else:
            if is_prev_uc:
                ccs += ci.upper()
                is_prev_uc = False
            else:
                ccs += ci
    return ccs


def first_char_lower(s: str) -> str:
    """Make first char lowercase"""
    return s[0:1].lower() + s[1:]


def first_char_upper(s: str) -> str:
    """Make first char uppercase"""
    return s[0:1].upper() + s[1:]


def gen_tokens(cnt: int, token: str) -> str:
    '''
    Generate N tokens joined as string
    '''
    s = ""
    for _ in range(cnt):
        s += token
    return s


def spaces(cnt: int) -> str:
    '''
    Generate N spaces characters joined as string
    '''
    if cnt < 1:
        return ""
    return gen_tokens(cnt, " ")


def str_width(s: str) -> int:
    '''
    Calculate the actual rendered width of string (i.e., actual width of half/full width characters)
    '''
    if not s:
        return 0
    l = 0
    for i in range(len(s)):
        w = unicodedata.east_asian_width(s[i])
        l += 2 if w in ['W', 'F', 'A'] else 1
    return l


def today_str() -> str:
    '''
    Print today in forms of yyyyMMdd
    '''
    return date.today().strftime('%Y%m%d')


def env_print(key, value):
    '''
    Print env conf in forms of 'KEY:VALUE'
    '''
    prop = key + ":"
    print(f"{prop:40}{value}")


def random_digits(n: int) -> str:
    '''
    Generate random digits
    '''
    return ''.join(random.choices(string.digits, k=n))


def random_str(n: int) -> str:
    '''
    Generate random string
    '''
    return ''.join(random.choices(string.ascii_letters, string.digits, k=n))


def quote(s: str, mark: str = "'") -> str:
    '''
    Quote a string
    '''
    if not s:
        return ""
    return mark + s.strip() + mark


def escape_quote(s: str, quote: str = "'", escape: str = '\\') -> str:
    '''
    Escape quote with \\ prefix
    '''
    return s.replace(quote, f'{escape}{quote}')


def space_tokenize(s: str) -> list[str]:
    '''
    Split string into tokens, spaces in quoted string are preserved
    '''
    return shlex.split(s, posix=False)


def index_list(ar: list[str]) -> dict[str]:
    '''
    Build index for the values in list, returns a dict where K is the value, V is the index
    '''
    idx = {}
    for i in range(len(ar)):
        idx[ar[i]] = i
    return idx


def print_table(col: list[str], rows: list[list[str]], include_line_end: bool = True, exclude_cols: set[str] = None) -> str:
    '''
    Convert table to a readable string
    '''
    width = str_width
    printed = []

    # max length among the rows
    indent: dict[int][int] = {}
    for i in range(len(col)):
        indent[i] = width(col[i])
    for r in rows:
        for i in range(len(col)):
            indent[i] = max(indent[i], width(r[i]))

    col_title = "| "
    col_sep = "|-"
    for i in range(len(col)):
        if col[i] is None:
            col[i] = ''
        if exclude_cols and col[i] in exclude_cols:
            continue
        col_title += col[i] + spaces(indent[i] - width(col[i]) + 1) + " | "
        col_sep += gen_tokens(indent[i] + 1, "-") + "-|"
        if i < len(col) - 1:
            col_sep += "-"
    printed.append(col_sep + "\n" + col_title + "\n" + col_sep)

    for r in rows:
        row_ctn = "| "

        for i in range(len(col)):
            if exclude_cols and col[i] in exclude_cols:
                continue
            rv = r[i]
            if rv is None:
                rv = ''
            line = rv + spaces(1 + indent[i] - width(rv))
            if i < len(col) - 1 or include_line_end:
                line += " | "
            row_ctn += line
        printed.append(row_ctn)
    printed.append(col_sep)
    return "\n".join(printed)


def get_platform():
    '''
    Get current os's platform, can be any one of [ 'darwin', 'win64', 'win32', 'wsl', 'linux' ]
    '''
    # https://stackoverflow.com/questions/434597/open-document-with-default-os-application-in-python-both-in-windows-and-mac-os
    if sys.platform == 'linux':
        try:
            proc_version = open('/proc/version').read()
            if 'Microsoft' in proc_version:
                return 'wsl'
        except:
            pass
    return sys.platform


def default_open(filename):
    '''
    Open file with default application
    '''
    # https://stackoverflow.com/questions/434597/open-document-with-default-os-application-in-python-both-in-windows-and-mac-os
    platform = get_platform()
    if platform == 'darwin':
        subprocess.call(('open', filename))
    elif platform in ['win64', 'win32']:
        os.startfile(filename.replace('/', '\\'))
    elif platform == 'wsl':
        subprocess.call('cmd.exe /C start'.split() + [filename])
    else:                                   # linux variants
        subprocess.call(('xdg-open', filename))


def quote_list(l: list[str], quote: str = "'"):
    '''
    Quote each item in the list with a single quote (by default), a new list is returned
    '''
    j = []
    for i in range(len(l)):
        j.append(f"{quote}{l[i]}{quote}")
    return j


def rev_idx(ele: list[str], val: set[str] = None) -> dict[str]:
    '''
    Build index of val in ele, if val is None, idx for all values in ele is built
    '''
    idx = {}
    for i in range(len(ele)):
        if val is None or ele[i] in val:
            idx[ele[i]] = i
    return idx


def filter_by_idx(l: list[str], idx: set[int]) -> list[str]:
    '''
    Filter items in l by index in idx, a new list with filtered values is returned
    '''
    r = []
    for i in range(len(l)):
        if i in idx:
            continue
        r.append(l[i])
    return r


def setup_completer():
    '''
    Introduce a word completer to readline
    '''
    readline.parse_and_bind("tab: complete")
    readline.set_completer(completer)
    global completer_candidates
    completer_candidates = set()


def completer(text, state):
    '''
    Completer function, used by prep_completer() for readline

    Internally, it uses a global variable named completer_candidates, which is basically a set of string
    '''
    global completer_candidates
    if not text:
        return None
    options = [cmd for cmd in completer_candidates if cmd.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None


def feed_completer_nested(rl: list[list]):
    '''
    feed words to completer
    '''
    for r in rl:
        for v in r:
            feed_completer_nested(v)


def feed_completer(word: str):
    '''
    feed words to completer
    '''
    global completer_candidates
    if not word:
        return
    completer_candidates.add(word)


def defval(v, default_val) -> any:
    if not v:
        return default_val
    return v


def walk(dic, *nested_fields: str) -> any:
    '''
    Walk the dictionary, return None if not found.
    '''
    return dict_get(dic, '.'.join(nested_fields))


def dict_get(d, expr: str, default_val=None) -> any:
    '''
    Retrieve value from a dict recursively by providing a dot delimited expression, e.g., name.key.juice
    '''
    if not expr or not d:
        return default_val
    if type(d) != dict:
        return default_val
    sp = expr.split(".", 1)

    if not sp[0] in d:
        d = None
    else:
        d = d[sp[0]]

    if len(sp) > 1:
        return dict_get(d, sp[1], default_val)
    else:
        return d if d else default_val


def str_matches(t: str, v: str) -> bool:
    """Check whether two string matches ignore cases"""
    return t.casefold() == v.casefold()


class DictWalker():
    def __init__(self, target: dict):
        self.target = target

    def get(self, expr: str, default_val=None) -> any:
        return dict_get(self.target, expr, default_val)
