data = range(-15, 15)

result = [number for number in data if number %
          3 == 0 and number > 0 and not number % 4 == 0]

print(result)
