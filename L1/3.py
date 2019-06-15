print('Пациент')
name = input('Имя: ')
second_name = input('Фамилия: ')
age = int(input('Возраст: '))
weight = int(input('Вес, кг: '))

condition = 'без особенностей'

if age < 30 and weight >= 50 and weight <= 120:
    condition = 'хорошее состояние'

if age > 30 and (weight < 50 or weight > 120):
    condition = 'следует заняться собой'

if age > 40 and (weight < 50 or weight > 120):
    condition = 'следует обратится к врачу!'

print('{} {}, {} лет, вес {} - {}'
      .format(name, second_name, age, weight, condition))
