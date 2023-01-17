#!/usr/bin/env python3
import random
import math
from brain_game.scripts.cli import welcome_user


def gcd():
    user_name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    index = 0
    while index < 3:
        x = random.randint(1, 50)
        y = random.randint(1, 50)
        z = math.gcd(x, y)
        print('Question: ', x, y)
        answer = input('Your answer: ')
        result = 'Correct!'
        if answer == result:
            index += 1
            print(result)
        elif answer != z:
            print(f"'{answer}' + is wrong answer ;(. "
                  f"Correct answer was {z}. Let's try again, {user_name}!")
            break
    if index == 3:
        end = print(f"Congratulations, {user_name}!")
        return end


if __name__ == '__main__':
    gcd()
