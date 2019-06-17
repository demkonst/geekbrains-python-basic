my_list_1 = [2, 2, 5, 12, 8, 2, 12]

distincts = {}
result = []
for n in my_list_1:
    if n in distincts:
        distincts[n] = False
    else:
        distincts[n] = True

for n in distincts: 
    if distincts[n]:
        result.append(n)

print(result)
