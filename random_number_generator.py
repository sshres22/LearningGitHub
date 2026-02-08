import random

def generate_random_number(limit):
    return random.randint(0, limit)

if __name__ == '__main__':
    while True:
        try:
            user_input = int(input('Enter a number between 0 and 100: '))
            if 0 <= user_input <= 100:
                random_number = generate_random_number(user_input)
                print(f'Random number between 0 and {user_input}: {random_number}')
                break
            else:
                print('Please enter a number between 0 and 100!')
        except ValueError:
            print('Invalid input! Please enter a valid number.')