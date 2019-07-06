import sys
import os
import game
from core import copy_file, create_file, create_folder, delete_file, get_list, save_info

def d1():
    print(123)

def d2(d1):
    d1()
d2(d1)
try:
    cmd = sys.argv[1]
except IndexError:
    cmd = 'help'

if cmd == 'copy_file':
    try:
        name = sys.argv[2]
        new_name = sys.argv[3]
    except:
        print('Недостаточно параметров')
    else:
        copy_file(name, new_name)
elif cmd == 'create_file':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Недостаточно параметров')
    else:
        create_file(name)
elif cmd == 'create_folder':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Недостаточно параметров')
    else:
        create_folder(name)
elif cmd == 'delete_file':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Недостаточно параметров')
    else:
        delete_file(name)
elif cmd == 'get_list':
    get_list()
elif cmd == 'chdir':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Недостаточно параметров')
    else:
        os.chdir(name)
elif cmd == 'game':
    game.play_game()
elif cmd == 'help':
    print('Команды:')
    print('copy_file - копирование файла или папки')
    print('create_file - создание файла')
    print('create_folder - создание папки')
    print('delete_file - удаление файла или папки')
    print('get_list - список файлов и папок')
    print('game - игра "Угадай число"')

save_info('end')
