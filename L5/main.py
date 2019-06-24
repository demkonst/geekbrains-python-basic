import dirs
import random_el

dirs.create_dirs()

input('Директории созданы, введите любой символ для продолжения')

dirs.delete_dirs()

input('Директории удалены, введите любой символ для продолжения')

items = [75, 48, 345, 7638, 6587, 256]
print(random_el.get_random_element(items))
