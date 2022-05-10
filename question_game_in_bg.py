import random

questions = ['Кога е основана Българската държава?', 'Колко е 2 x 2?', 'Коя е най-голямата по площ държава в света?',
             'През коя година България се е освободила от турско робство?', 'Кой е написал стихотворението "Майце си?"',
             'Коя е държавата с най-многобройното население в света?']
guess_win_counter = 0
guess_lose_counter = 0
answered_questions = []
points = 0

while True:
    question = random.choice(questions)

    if guess_win_counter == 1:
        points += 5
        if guess_lose_counter == 1:
            points -= 1
        elif guess_lose_counter == 2:
            points -= 2
        elif guess_lose_counter == 3:
            points -= 3
        elif guess_lose_counter == 4:
            points -= 4
    elif guess_win_counter == 2:
        points += 10
        if guess_lose_counter == 1:
            points -= 1
        elif guess_lose_counter == 2:
            points -= 2
        elif guess_lose_counter == 3:
            points -= 3
        elif guess_lose_counter == 4:
            points -= 4
    elif guess_win_counter == 3:
        points += 20
        if guess_lose_counter == 1:
            points -= 1
        elif guess_lose_counter == 2:
            points -= 2
        elif guess_lose_counter == 3:
            points -= 3
        elif guess_lose_counter == 4:
            points -= 4

    if guess_win_counter == 3:
        print('!!!ТИ СПЕЧЕЛИ ИГРАТА!!!')
        print(f'Твоите точки са: {points}')
        break

    if guess_lose_counter == 5:
        print('ТИ ЗАГУБИ ИГРАТА.')
        break

    if question not in answered_questions:
        answered_questions.append(question)
        print(question)
    else:
        continue

    if question == 'Кога е основана Българската държава?':
        user_answer = input('Въведете отговор: ')

        if user_answer == '681':
            print('Ти позна!\n')
            guess_win_counter += 1
            continue
        else:
            print('Грешен отговор.\n')
            guess_lose_counter += 1
            continue

    elif question == 'Колко е 2 x 2?':
        user_answer = input('Въведете отговор: ')

        if user_answer == '4':
            print('Ти позна!\n')
            guess_win_counter += 1
            continue
        else:
            print('Грешен отговор.\n')
            guess_lose_counter += 1
            continue

    elif question == 'Коя е най-голямата по площ държава в света?':
        user_answer = input('Въведете отговор: ')

        if user_answer == 'Русия':
            print('Ти позна!\n')
            guess_win_counter += 1
            continue
        else:
            print('Грешен отговор.\n')
            guess_lose_counter += 1
            continue

    elif question == 'През коя година България се е освободила от турско робство?':
        user_answer = input('Въведете отговор: ')

        if user_answer == '1878':
            print('Ти позна!\n')
            guess_win_counter += 1
            continue
        else:
            print('Грешен отговор.\n')
            guess_lose_counter += 1
            continue

    elif question == 'Кой е написал стихотворението "Майце си?"':
        user_answer = input('Въведете отговор: ')

        if user_answer == 'Христо Ботев':
            print('Ти позна!\n')
            guess_win_counter += 1
            continue
        else:
            print('Грешен отговор.\n')
            guess_lose_counter += 1
            continue

    elif question == 'Коя е държавата с най-многобройното население в света?':
        user_answer = input('Въведете отговор: ')

        if user_answer == 'Китай':
            print('Ти позна!\n')
            guess_win_counter += 1
            continue
        else:
            print('Грешен отговор.\n')
            guess_lose_counter += 1
            continue
