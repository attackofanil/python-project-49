#!/usr/bin/env python3
import random
from random import randint
from brain_game.scripts.brain_games import greetings
from brain_game.scripts.cli import welcome_user


def calc():
    name = welcome_user()
    print('What is the result of the expression?')
    counter = 0
    while counter < 3:
        first_number = random.randint(50, 100)
        second_number = random.randint(1, 50)
        expression = ['+', '-', '*']
        end = expression[randint(0, len(expression) - 1)]
        print(f"Question: {first_number} {end} {second_number}")
        total = ''
        if end == '+':
            total = first_number + second_number
        elif end == '-':
            total = first_number - second_number
        elif end == '*':
            total = first_number * second_number
        answer = int(input('Your answer: '))
        result = 'Correct!'
        if answer == total:
            counter += 1
            print(result)
        elif answer != total:
            print(f"'{answer}' + is wrong answer ;(.\
 Correct answer was {total}. Let's try again, {name}!")
            break
    if counter == 3:
        end = print(f"Congratulations, {name}!")
        return end


if __name__ == '__main__':
    calc()
