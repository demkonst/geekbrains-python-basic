my_list_1 = [2, 5, 5, 8, 2, 12, 12, 4, 17]
my_list_2 = [2, 7, 12, 3]

for item in my_list_2:
    while item in my_list_1:
        my_list_1.remove(item)

print(my_list_1)