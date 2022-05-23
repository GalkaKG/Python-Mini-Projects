import random

print('Здрасти! :) Моля въведи името си:')
name = input()
print(f'Здравей, {name}. Сега ще играем една игра. В нея ти трябва да познаеш името '
      f'за което си мисля в момента.')
print('Не се притеснявай! Сега ще те оставя да напишеш 3 имена и ще си избера едно от тях.')
print('След това ти трябва да познаеш името, за което си мисля в момента.')
print('Моля въведи първото име: ')
name1 = input()
print('Моля въведи второто име: ')
name2 = input()
print('Моля въведи третото име: ')
name3 = input()

names = [name1, name2, name3]

print(f'Добре {name}. Благодаря ти, че въведе тези имена!')
secret_name = random.choice(names)

not_guessed = False

for _ in range(3):
    print('Сега въведи името, за което си мисля: ')
    answer = input()

    if answer == secret_name:
        print(f'Браво, {name}!\nПозна :)))))')
        break
    else:
        print(f'Грешка. Името за което си мислех беше {secret_name}.\n')
        not_guessed = True

if not_guessed:
    print('ИГРАТА ПРИКЛЮЧИ.')
