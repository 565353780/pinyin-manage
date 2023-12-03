from pinyin_sort.Data.info import Info
from pinyin_sort.Method.io import loadSplitInfoStrLists
from pinyin_sort.Method.sort import toPinyin, sortFunc

class InfoManager(object):
    def __init__(self, txt_file_path: str=None, edit_info_str_list_func=None) -> None:
        self.info_list = []
        self.sort_info_list = []

        if txt_file_path is not None and edit_info_str_list_func is not None:
            self.loadFile(txt_file_path, edit_info_str_list_func)
        return

    def reset(self) -> bool:
        self.info_list = []
        self.sort_info_list = []
        return True

    def __len__(self) -> int:
        return len(self.info_list)

    def isValid(self) -> bool:
        return len(self.info_list) > 0

    def addInfo(self, key: str, str_list: [], key_to_pinyin: bool=True) -> bool:
        if key_to_pinyin:
            key = toPinyin(key)

        self.info_list.append(Info(key, str_list))
        return True

    def sort(self, inverse=False) -> bool:
        self.sort_info_list = sorted(self.info_list, key=sortFunc)
        return True

    def loadFile(self, txt_file_path: str, edit_info_str_list_func) -> bool:
        info_str_lists = loadSplitInfoStrLists(txt_file_path)

        if info_str_lists is None:
            print('[ERROR][InfoManager::loadFile]')
            print('\t loadSplitInfoStrLists failed!')
            return False

        for info_str_list in info_str_lists:
            edit_info_str_list = edit_info_str_list_func(info_str_list)

            self.addInfo(edit_info_str_list[0], edit_info_str_list[1:])
        return True

    def toSubInfoManager(self, tag_str: str):
        sub_info_manager = InfoManager()

        for info in self.info_list:
            if info.isContainTag(tag_str):
                sub_info_manager.addInfo(info.key, info.str_list)
        return sub_info_manager

    def saveInfo(self, save_file_path: str, info_to_str_func, need_sort: bool=True) -> bool:
        if need_sort:
            self.sort()

            with open(save_file_path, 'w') as f:
                for sort_info in self.sort_info_list:
                    f.write(info_to_str_func(sort_info))

            return True

        with open(save_file_path, 'w') as f:
            for info in self.info_list:
                f.write(info_to_str_func(info))
        return True
