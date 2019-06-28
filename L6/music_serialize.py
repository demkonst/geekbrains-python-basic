import pickle
import json

data = {
    'name': 'Г.М.О.',
    'tracks': ['Последний месяц осени', 'Шапито'],
    'Albums': [
        {'name': 'Делать панк-рок', 'year': 2016},
        {'name': 'Шапито', 'year': 2014}
    ]
}

data_bytes = pickle.dumps(data)
print(data_bytes)

data_json = json.dumps(data)
print(data_json)

with open('group.pickle', 'wb') as f:
    pickle.dump(data, f)

with open('group.json', 'w', encoding='utf-8') as f:
    json.dump(data, f)
