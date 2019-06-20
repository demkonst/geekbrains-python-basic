import random
from time import sleep


def damage_armored(who, whom):
    return int(who['damage'] / whom['armor'])


def attack(who, whom):
    whom['health'] -= damage_armored(who, whom)
    print('{} ударил {}. Осталось {} здоровья'.format(
        who['name'], whom['name'],  whom['health']))


def randomize_damage(who):
    who['damage'] += max(random.randint(-3, 3), 1)


player_name = input('Имя игрока: ')
enemy_name = input('Имя врага: ')

player = {
    'name': player_name,
    'health': 100,
    'armor': 1.3,
    'damage': 5
}

enemy = {
    'name': enemy_name,
    'health': 100,
    'armor': 1.2,
    'damage': 5
}

while player['health'] > 0 and enemy['health'] > 0:
    randomize_damage(player)
    randomize_damage(enemy)
    attack(player, enemy)
    attack(enemy, player)
    sleep(0.2)

if(player['health'] <= 0 and enemy['health'] <= 0):
    print('Убиты оба')
elif(player['health'] <= 0):
    print('{} убит'.format(player['name']))
elif(enemy['health'] <= 0):
    print('{} убит'.format(enemy['name']))
