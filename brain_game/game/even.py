#!/usr/bin/env python3
import random
from brain_game.scripts.cli import welcome_user
from brain_game.scripts.brain_games import main


def even():
    index = 0
    user_name = welcome_user()
    print(f'Answer "yes" if the number is even, otherwise answer "no".')
    while index < 3:
        x = random.randint(1, 100)
        print('Question: ', x)
        answer = input('Your answer: ')
        result = 'Correct!'
        if (x % 2 == 0 and answer == 'yes') or (x % 2 != 0 and answer == 'no'):
            index += 1
            print(result)
        elif x % 2 == 0 and answer != 'yes':
            print(f"'{answer}' + is wrong answer ;(. Correct answer was 'yes'. Let's try again, {user_name}!")
            break
        elif x % 2 != 0 and answer != 'no':
            print(f"'{answer}' + is wrong answer ;(. Correct answer was 'no'. Let's try again, {user_name}!")
            break

    if index == 3:
        print(f"Congratulations, {user_name}!")
        return


if __name__ == '__main__':
    even()
