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
