import random

print('Загадайте число от 1 до 100')
print('Если ваше число меньше предложенного, введите "<"')
print('Если ваше число больше предложенного, введите ">"')
print('Если ваше число равно предложенного, введите "="')

start = 1
end = 100
while True:
    if(end-start <= 1):
        print('Вы ошиблись во вводе')
        break

    n = int(start + (end-start)/2)
    print('{}?'.format(n))
    comp = input()
    if(comp == '<'):
        end = n
    elif(comp == '>'):
        start = n
    elif(comp == '='):
        print('Мы отгадали число')
        break
