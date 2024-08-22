import json

# 读取文件内容
with open('tq/形式与政策.txt', 'r', encoding='utf-8') as file:
    questions_text = file.read()


# 解析题库内容的函数
def parse_questions(questions_text):
    question_list = []
    question_lines = questions_text.strip().split('\n\n')

    for question in question_lines:
        question_json = {}
        lines = question.strip().split('\n')
        length = len(lines)
        answer = lines[-1].split(': ', 1)[1]
        question_json["name"] = lines[0]
        if length == 2:
            question_json["type"] = "判断题"
        else:
            if len(answer) == 1:
                question_json["type"] = "单选题"
            else:
                question_json["type"] = "多选题"
        question_json['options'] = []
        for index,line in enumerate(lines):
            if index == 0 or index == len(lines) - 1:
                continue
            option = line.split(': ', 1)

            question_json['options'].append({option[0]: option[1]})
        question_json["answer"] = answer
        question_list.append(question_json)

    return question_list


# 转换为JSON格式
parsed_questions = parse_questions(questions_text)
json_output = json.dumps(parsed_questions, ensure_ascii=False, indent=4)

# 输出JSON
print(json_output)

# 将JSON保存到文件
with open('tq/形式与政策.json', 'w', encoding='utf-8') as f:
    f.write(json_output)
