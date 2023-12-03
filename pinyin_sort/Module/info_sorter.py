from pinyin_sort.Data.info import Info
from pinyin_sort.Method.sort import toPinyin, sortFunc

class InfoSorter(object):
    def __init__(self) -> None:
        self.info_list = []
        self.sort_info_list = []
        return

    def reset(self) -> bool:
        self.info_list = []
        self.sort_info_list = []
        return True

    def __len__(self) -> int:
        return len(self.info_list)

    def addInfo(self, key: str, str_list: [], key_to_pinyin: bool=True) -> bool:
        if key_to_pinyin:
            key = toPinyin(key)

        self.info_list.append(Info(key, str_list))
        return True

    def sort(self, inverse=False) -> bool:
        self.sort_info_list = sorted(self.info_list, key=sortFunc)
        return True
