data = range(-7, 7)

result = [number if number < 0 else number**2 for number in data]

print(result)
