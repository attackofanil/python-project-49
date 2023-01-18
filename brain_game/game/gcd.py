#!/usr/bin/env python3
import random
import math
import prompt
from brain_game.scripts.cli import welcome_user


def gcd():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    counter = 0
    while counter < 3:
        first_number = random.randint(1, 50)
        second_number = random.randint(1, 50)
        expression = math.gcd(first_number, second_number)
        print(f"Question: {first_number} {second_number}")
        answer = int(prompt.string('Your answer: '))
        result = 'Correct!'
        if answer == expression:
            counter += 1
            print(result)
        elif answer != expression:
            print(f"'{answer}' + is wrong answer ;(. "
                  f"Correct answer was {expression}. Let's try again, {name}!")
            break
    if counter == 3:
        end = print(f"Congratulations, {name}!")
        return end


if __name__ == '__main__':
    gcd()
