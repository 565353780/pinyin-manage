from pinyin_sort.Module.info_sorter import InfoSorter

def getQuestions(txt_file_path):
    lines = []

    with open(txt_file_path, 'r') as f:
        lines = f.readlines()

    question_list = []

    question = []

    current_idx = 1

    num = 0
    for line in lines:
        line = line.replace(' ', '')

        if line == '\n':
            question_list.append(question)
            question = []
            current_idx += 1
            continue

        if len(question) == 0:
            num += 1

            q = line.split(str(num) + '.')[1]
            # question.append(num)
            question.append(q)
            continue

        question.append(line)

    questions = InfoSorter()

    for question in question_list:
        questions.addInfo(question[0], question)
    return questions

def getSplitQuestions(questions, key):
    split_questions = InfoSorter()

    for question in questions.info_list:
        q_type = question.str_list[-1]

        if key not in q_type:
            continue

        split_questions.info_list.append(question)
    return split_questions

def saveQuestions(questions, save_file_path):
    questions.sort()

    with open(save_file_path, 'w') as f:
        for question in questions.sort_info_list:
            f.write(question.key[0] + question.toStr())
            f.write('\n')
    return True

def demo():
    data_folder_path = '/Users/fufu/Downloads/姑姑/'

    questions = getQuestions(data_folder_path + 'data.txt')

    panduan_questions = getSplitQuestions(questions, '判断题')
    danxuan_questions = getSplitQuestions(questions, '单选题')
    duoxuan_questions = getSplitQuestions(questions, '多选题')

    print(len(questions))
    print(len(panduan_questions), '+', len(danxuan_questions), '+', len(duoxuan_questions), '=',
          len(panduan_questions) + len(danxuan_questions) + len(duoxuan_questions))

    saveQuestions(questions, data_folder_path + 'all.txt')
    saveQuestions(panduan_questions, data_folder_path + 'panduan.txt')
    saveQuestions(danxuan_questions, data_folder_path + 'danxuan.txt')
    saveQuestions(duoxuan_questions, data_folder_path + 'duoxuan.txt')
    return True
