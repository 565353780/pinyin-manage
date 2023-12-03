import os
from typing import Union

def loadSplitInfoStrLists(txt_file_path: str) -> Union[None, list]:
    if not os.path.exists(txt_file_path):
        print('[ERROR][io::getSplitInfoStrLists]')
        print('\t txt file not exist!')
        print('\t txt_file_path:', txt_file_path)
        return None

    lines = []

    with open(txt_file_path, 'r') as f:
        lines = f.readlines()

    info_str_lists = []

    info_str = []

    for line in lines:
        if line == '\n':
            info_str_lists.append(info_str)
            info_str = []
            continue

        info_str.append(line)

    if len(info_str) > 0:
        info_str_lists.append(info_str)

    return info_str_lists
