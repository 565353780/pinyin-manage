class Info(object):
    def __init__(self, key: str='', str_list: list=[]) -> None:
        self.key = key
        self.str_list = str_list
        return

    def toStr(self) -> str:
        info_str = ''
        for info in self.str_list:
            info_str += info
        return info_str
