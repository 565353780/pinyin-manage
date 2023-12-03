from pinyin_manage.Module.info_manager import InfoManager

def demo():
    data_folder_path = '/Users/fufu/Downloads/姑姑/'
    need_sort = True

    def editInfoStrListFunc(info_str_list):
        dot_position = info_str_list[0].find('.')
        split_info = info_str_list[0][:(dot_position+1)]
        key_without_num = info_str_list[0].split(split_info)[1]

        edit_info_str_list = []

        edit_info_str_list.append(key_without_num)
        edit_info_str_list.append(key_without_num)

        for i in range(1, len(info_str_list)):
            edit_info_str_list.append(info_str_list[i])

        return edit_info_str_list

    def editInfoFunc(info):
        return info.key[0] + info.toStr() + '\n'

    info_manager = InfoManager(data_folder_path + 'data.txt', editInfoStrListFunc)

    panduan_info_manager = info_manager.toSubInfoManager('判断题')
    danxuan_info_manager = info_manager.toSubInfoManager('单选题')
    duoxuan_info_manager = info_manager.toSubInfoManager('多选题')

    print(len(info_manager))
    print(len(panduan_info_manager), '+', len(danxuan_info_manager), '+', len(duoxuan_info_manager), '=',
          len(panduan_info_manager) + len(danxuan_info_manager) + len(duoxuan_info_manager))

    info_manager.saveInfo(data_folder_path + 'all.txt', editInfoFunc)
    panduan_info_manager.saveInfo(data_folder_path + 'panduan.txt', editInfoFunc, need_sort)
    danxuan_info_manager.saveInfo(data_folder_path + 'danxuan.txt', editInfoFunc, need_sort)
    duoxuan_info_manager.saveInfo(data_folder_path + 'duoxuan.txt', editInfoFunc, need_sort)
    return True
