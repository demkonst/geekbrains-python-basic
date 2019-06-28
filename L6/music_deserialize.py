import pickle
import json

with open('group.pickle', 'rb') as f:
    data = pickle.load(f)
    print(data)


with open('group.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(data)
