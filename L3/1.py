import random

print('Загадайте число от 1 до 100')
print('Если предложенное число меньше загаданного, введите "<"')
print('Если предложенное число больше загаданного, введите ">"')
print('Если предложенное число равно загаданному, введите "="')

start = 1
end = 100
while True:
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
