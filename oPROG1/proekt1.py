score = 0

questions = [
    "Вопрос 1: Вам нравится программировать?: ",
    "Вопрос 2: Вы знакомы с языком Python?: ",
    "Вопрос 3: Вам нравится математика?: ",
    "Вопрос 4: Вы любите работать с данными?: ",
    "Вопрос 5: Вам нравится решать сложные задачи?: "
]

print("")

for question in questions:
    answer = input(question)
    while True:
        if answer.lower() == 'да':
            score += 2
            break
        elif str(answer) == 'Нет' or str(answer) == 'нет':
            score += 1
            break
        else:
            print("Введите ответ да или нет!")
            answer = input(question)



if score <= 5:
    print("Ваш результат: Низкий уровень")
elif score <= 8:
    print("Ваш результат: Средний уровень")
else:
    print("Ваш результат: Высокий уровень")

print("Вы набрали", score, "баллов")
