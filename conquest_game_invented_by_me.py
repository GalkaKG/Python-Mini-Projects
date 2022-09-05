import random
 
countries = ['Romania', 'Serbia', 'Macedonia', 'Greece', 'Turkey', 'Albania', 'Hungary', 'Austria', 'Germany', 'France']
conquest_country = []
 
gold_player = 0
power_player = 0
gold_computer = 0
power_computer = 0
next_will_be = ''
 
who_s_first = ['player', 'computer']
first_will_be = random.choice(who_s_first)
your_name = input('What is your name?\n')
print('***********************************************************************')
print(f'* Hello, {your_name}. Welcome to the game "Conquest"! I wish you good luck! *')
print('***********************************************************************\n')
print(f'{first_will_be} will start to play first.')
 
for _ in range(0, 30):
    conquest = random.choice(countries)
    country = conquest
 
    if country not in conquest_country:
        conquest_country.append(conquest)
    else:
        continue
 
    if next_will_be:
        print(f'Is your turn {next_will_be}!')
    print(f'You will fight for {country}.\n')
 
    if country in ['Romania', 'Serbia', 'Macedonia', 'Albania']:
        if first_will_be == 'computer':
            gold_computer += 100
            power_computer += 1000
        elif first_will_be == 'player':
            gold_player += 100
            power_player += 1000
            fight = input('Press "f" to fight: ')
        if next_will_be == 'computer':
            gold_computer += 100
            power_computer += 1000
        elif next_will_be == 'player':
            gold_player += 100
            power_player += 1000
            print('Press "f" to fight: ')
            fight = input()
 
    elif country in ['Greece', 'Turkey', 'Hungary', 'Austria']:
        if first_will_be == 'computer':
            gold_computer += 150
            power_computer += 1500
        elif first_will_be == 'player':
            gold_player += 150
            power_player += 1500
            fight = input('Press "f" to fight: ')
        if next_will_be == 'computer':
            gold_computer += 150
            power_computer += 1500
        elif next_will_be == 'player':
            gold_player += 150
            power_player += 1500
            fight = input('Press "f" to fight: ')
 
    elif country in ['Germany', 'France']:
        if first_will_be == 'computer':
            gold_computer += 200
            power_computer += 2000
        elif first_will_be == 'player':
            gold_player += 200
            power_player += 2000
            fight = input('Press "f" to fight: ')
        if next_will_be == 'computer':
            gold_computer += 200
            power_computer += 2000
        elif next_will_be == 'player':
            gold_player += 200
            power_player += 2000
            fight = input('Press "f" to fight: ')
 
    if next_will_be == 'computer':
        next_will_be = 'player'
    else:
        next_will_be = 'computer'
 
    if first_will_be == 'computer':
        next_will_be = 'player'
        first_will_be = ''
    elif first_will_be == 'player':
        next_will_be = 'computer'
        first_will_be = ''
 
print('Now you will see the RESULT:')
print('----------------------------')
print(f'Player power is {power_player} and gain {gold_player} gold.')
print(f'Computer power is {power_computer} and gain {gold_computer} gold.')
 
if gold_player > gold_computer:
    gold_player += gold_computer
    print('Player will use the all gold for refreshing Bulgarian economy.')
    print(f'Total gold: {gold_player}.')
elif gold_computer > gold_player:
    print('Computer doesn`t need the gold. Will give it all for charity!')
elif gold_player == gold_computer:
    print(f'Player and computer will give {gold_player + gold_computer} gold for charity.')
 
if power_player > power_computer:
    print(f'Player you win the game and join all the territories of the countries to Bulgaria!')
elif power_computer > power_player:
    print(f'Computer wins this game. But one game over doesn`t mean the war is won!')
elif power_player == power_computer:
    print('You will need to fight again!!!')
