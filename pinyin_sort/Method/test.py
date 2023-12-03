from pinyin_sort.Module.info_sorter import InfoSorter

def getQuestions(txt_file_path):
    lines = []

    with open(txt_file_path, 'r') as f:
        lines = f.readlines()

    questions = []

    question = []

    current_idx = 1

    num = 0
    for line in lines:
        line = line.replace(' ', '')

        if line == '\n':
            questions.append(question)
            question = []
            current_idx += 1
            continue

        if len(question) == 0:
            num += 1

            q = line.split('\n')[0].split(str(num) + '.')[1]
            q_py = to_pinyin(q)

            question.append(q_py)
            question.append(num)
            question.append(q)
            continue

        question.append(line.split('\n')[0])

    questions = InfoSorter()

    for question in questions:
        questions.addInfo(question[0], question[2:])
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
        for question in questions.info_list:
            f.write(question.key[0])
            for i in range(2, len(question.str_list)):
                f.write(question.str_list[i] + '\n')
            f.write('\n')
    return True

questions = getQuestions('./data.txt')

panduan_questions = getSplitQuestions(questions, '判断题')
danxuan_questions = getSplitQuestions(questions, '单选题')
duoxuan_questions = getSplitQuestions(questions, '多选题')

print(len(questions))
print(len(panduan_questions))
print(len(danxuan_questions))
print(len(duoxuan_questions))

saveQuestions(questions, './all.txt')
saveQuestions(panduan_questions, './panduan.txt')
saveQuestions(danxuan_questions, './danxuan.txt')
saveQuestions(duoxuan_questions, './duoxuan.txt')
