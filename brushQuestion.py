import json

# 读取 JSON 文件内容
with open('tq/parse_test.json', 'r', encoding='utf-8') as file:
    questions = json.load(file)

# 循环遍历每一道题目
for question in questions:

    print(f"{question['type']}: {question['name']}")

    # 如果是选择题，输出选项
    if question['type'] in ['单选题', '多选题']:
        for option in question['options']:
            for key, value in option.items():
                print(f"{key}: {value}")

    # 等待用户输入答案
    if question['type'] == '判断题':
        user_answer = input("请输入你的答案(填对或错): ")
    else:
        user_answer = input("请输入你的答案: ")

    # 判断用户答案是否正确
    correct_answer = question['answer']
    if user_answer.upper() == correct_answer.upper():
        print("回答正确！\n")
    else:
        print(f"回答错误。正确答案是: {correct_answer}\n")

print("所有题目已完成。")

