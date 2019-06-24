import random


def get_random_element(items):
    return random.choice(items) if items else None


if __name__ == "__main__":
    items = [1, 5, 76, 45]
    print(get_random_element(items))

    items = []
    print(get_random_element(items))
