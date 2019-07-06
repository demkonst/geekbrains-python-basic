import os
import shutil
import datetime


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Папка уже существует')


def get_list(folders_only=False):
    files = os.listdir()
    if folders_only:
        files = [f for f in files if os.path.isdir(f)]
    print(files)


def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Папка уже существует')
    else:
        shutil.copyfile(name, new_name)


def save_info(msg):
    now = datetime.datetime.now()
    s = f'{now}: {msg}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(s+'\n')


if __name__ == "__main__":
    create_file('text.dat', '123')
    create_folder('test')
    get_list()
    get_list(True)

    copy_file('test', 'new_test')
    delete_file('new_test')
    copy_file('text.dat', 'new_text.dat')
    delete_file('new_text.dat')

    delete_file('test')
    delete_file('text.dat')
    save_info('text1')
