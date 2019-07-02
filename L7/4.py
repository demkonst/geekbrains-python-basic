def task_4(n):
    n = int(n)
    if(n < 0 or n > 100):
        raise Exception('Число вне допустимого диапазона')
    if(n == 13):
        raise Exception('Число 13 запрещено')

    return n**2


if __name__ == "__main__":
    n = input('Введите число от 0 до 100: ')
    try:
        print('Функция вернула {}'.format(task_4(n)))
    except Exception as e:
        print(e)
