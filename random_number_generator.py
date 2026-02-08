import random

def generate_random_number(limit):
    return random.randint(0, limit)

if __name__ == '__main__':
    user_input = int(input('Enter a number: '))
    random_number = generate_random_number(user_input)
    print(f'Random number between 0 and {user_input}: {random_number}')