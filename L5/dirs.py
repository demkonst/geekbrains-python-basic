import os


def get_full_path(i):
    return os.path.join(os.getcwd(), 'dir_{}'.format(i))


def create_dirs():
    for i in range(1, 9):
        path = get_full_path(i)
        if os.path.exists(path):
            continue
        os.mkdir(path)


def delete_dirs():
    for i in range(1, 9):
        path = get_full_path(i)
        if not os.path.exists(path):
            continue
        os.rmdir(path)


if __name__ == "__main__":
    while 1:
        c = input(
            'Введите \'c\' для создания директорий, \'d\' для их удаления, \'q\' для выхода: ')
        if c == 'c':
            create_dirs()
        elif c == 'd':
            delete_dirs()
        elif c == 'q':
            break
        else:
            pass
