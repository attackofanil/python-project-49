import prompt
import random
import prompt
from brain_game.scripts.cli import welcome_user


def prime():
    name = welcome_user()
    index = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while index < 3:
        x = random.randint(1, 100)
        result = 'Correct!'
        print(f"Question: {x}")
        answer = prompt.string('Your answer: ')
        counter = 0
        for i in range(2, x // 2 + 1):
            if x % i == 0:
                counter = counter + 1
        if counter <= 0 and answer == 'yes' or counter >= 0 and answer == 'no':
            index += 1
            print(result)
        else:
            print(f"'{answer}' + is wrong answer ;(. "
                  f"Correct answer was 'no'. Let's try again, {name}!")
            break

    if index == 3:
        print(f"Congratulations, {name}!")
        return


if __name__ == '__main__':
    prime()
