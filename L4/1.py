def desc(name, age, city):
    return '{}, {} год(а), проживает в городе {}'.format(name, age, city)


name = input('Имя: ')
age = input('Возраст: ')
city = input('Город: ')

print(desc(name, age, city))
