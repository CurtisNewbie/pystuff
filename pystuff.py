from datetime import *
import random
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
    return gen_tokens(cnt, " ")


def str_width(s: str) -> int:
    '''
    Calculate the actual rendered width of string (i.e., actual width of half/full width characters)
    '''
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
