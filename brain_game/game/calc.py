#!/usr/bin/env python3
import random
from brain_game.scripts.cli import welcome_user


def calc():
    name = welcome_user()
    print('What is the result of the expression?')
    counter = 0
    while counter < 3:
        first_number = random.randint(50, 100)
        second_number = random.randint(1, 50)
        expression = random.choice([' + ', ' - ', ' * '])
        question = str(first_number) + expression + str(second_number)
        print(f"Question: {question}")
        total = eval(question)
        answer = int(input('Your answer: '))
        result = 'Correct!'
        if answer == total:
            counter += 1
            print(result)
        else:
            print(f"'{answer}' + is wrong answer ;(.\
 Correct answer was {total}. Let's try again, {name}!")
            break
    if counter == 3:
        end = print(f"Congratulations, {name}!")
        return end


if __name__ == '__main__':
    calc()
