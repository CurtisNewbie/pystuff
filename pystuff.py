from datetime import *
import random
import shlex
import string
import unicodedata


def gen_tokens(cnt: int, token: str) -> str:
    '''
    Generate N tokens joined as string
    '''
    s = ""
    for i in range(cnt):
        s += token
    return s


def spaces(cnt: int) -> str:
    '''
    Generate N spaces characters joined as string
    '''
    if cnt < 1: return ""
    return gen_tokens(cnt, " ")


def str_width(s: str) -> int:
    '''
    Calculate the actual rendered width of string (i.e., actual width of half/full width characters)
    '''
    if not s: return 0
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


def index_list(ar : list[str]) -> dict[str]:
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
    indent : dict[int][int] = {}
    for i in range(len(col)): indent[i] = width(col[i])
    for r in rows:
        for i in range(len(col)): indent[i] = max(indent[i], width(r[i]))

    col_title = "| "
    col_sep = "|-"
    for i in range(len(col)):
        if col[i] is None: col[i] = ''
        if exclude_cols and col[i] in exclude_cols: continue
        col_title += col[i] + spaces(indent[i] - width(col[i]) + 1) + " | "
        col_sep += gen_tokens(indent[i] + 1, "-") + "-|"
        if i < len(col) - 1: col_sep += "-"
    printed.append(col_sep + "\n" + col_title + "\n" + col_sep)

    for r in rows:
        row_ctn = "| "

        for i in range(len(col)):
            if exclude_cols and col[i] in exclude_cols: continue
            rv = r[i]
            if rv is None: rv = ''
            line = rv + spaces(1 + indent[i] - width(rv))
            if i < len(col) - 1 or include_line_end: line += " | "
            row_ctn += line
        printed.append(row_ctn)
    printed.append(col_sep)
    return "\n".join(printed)