l1 = ['orange', 'apple', 'banana', 'grape', 'pear']
l2 = ['lime', 'grape', 'mango', 'banana', 'apple']

both = [fruit for fruit in l1 if fruit in l2]

print(both)