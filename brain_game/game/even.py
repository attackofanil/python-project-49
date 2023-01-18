#!/usr/bin/env python3
import random
from brain_game.scripts.cli import welcome_user
import prompt


def even():
    name = welcome_user()
    counter = 0
    print(f'Answer "yes" if the number is even, otherwise answer "no".')
    while counter  < 3:
        number = random.randint(1, 100)
        print(f"Question: {number})
        answer = prompt.string('Your answer: ')
        result = 'Correct!'
        if (number % 2 == 0 and answer == 'yes') or (number % 2 != 0 and answer == 'no'):
            counter  += 1
            print(result)
        elif number % 2 == 0 and answer != 'yes':
            print(f"'{answer}' + is wrong answer ;(. Correct answer was 'yes'. Let's try again, {name}!")
            break
        elif number % 2 != 0 and answer != 'no':
            print(f"'{answer}' + is wrong answer ;(. Correct answer was 'no'. Let's try again, {name}!")
            break

    if counter  == 3:
        print(f"Congratulations, {name}!")
        return


if __name__ == '__main__':
    even()
