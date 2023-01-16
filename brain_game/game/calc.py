import random
from random import randint
from brain_game.scripts.cli import welcome_user


def calc():
    print('What is the result of the expression?')
    index = 0
    while index < 3:
        x = random.randint(50, 100)
        y = random.randint(1, 50)
        z = ['+', '-', '*']
        end = z[randint(0, len(z) - 1)]
        print(f"Question: {x} {end} {y}")
        total = ''
        if end == '+':
            total = x + y
        elif end == '-':
            total = x - y
        elif end == '*':
            total = x * y
        answer = int(input('Your answer: '))
        result = 'Correct!'
        if answer == total:
            index += 1
            print(result)
        elif answer != total:
            print(f"'{answer}' + is wrong answer ;(.\
 Correct answer was {total}. Let's try again, {user_name}!")
            break
    if index == 3:
        print(f"Congratulations, {user_name}!")
        return


if __name__ == '__main__':
    user_name = welcome_user()
    print(f"Hello, {user_name}!")
    calc()
