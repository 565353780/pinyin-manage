import re
from itertools import chain
from pypinyin import pinyin, Style

def toPinyin(str_info):
    pinyin_str = ''.join(chain.from_iterable(pinyin(str_info, style=Style.TONE3)))
    pinyin_only = re.sub("([^\u0030-\u0039\u0041-\u007a])", '', pinyin_str)
    return pinyin_only

def sortFunc(info):
    return info.key
