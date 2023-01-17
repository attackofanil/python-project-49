import prompt
import random
from brain_game.scripts.cli import welcome_user


def prime():
    index = 0
    user_name = welcome_user()
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
                  f"Correct answer was 'no'. Let's try again, {user_name}!")
            break

    if index == 3:
        print(f"Congratulations, {user_name}!")
        return


if __name__ == '__main__':
    prime()
