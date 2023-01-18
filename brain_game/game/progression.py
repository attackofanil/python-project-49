import random
import prompt
from brain_game.scripts.cli import welcome_user
from random import randint


def progression():
    name = welcome_user()
    print('What number is missing in the progression?')
    trials = 0
    while trials < 3:
        start = randint(0, 10)
        end = randint(80, 100)
        step = randint(2, 10)
        sequence = list(range(start, end, step)[0:10])
        find_elem = str(random.choices(sequence, k=1))
        elem = int(find_elem[1:-1])
        index_elem = sequence.index(elem)
        sequence.pop(index_elem)
        str(sequence.insert(index_elem, '..'))
        print('Question: ' + " ".join(map(str, sequence)))
        answer = prompt.string('Your answer: ')
        result = 'Correct!'
        if answer == str(elem):
            trials += 1
            print(result)
        elif answer != elem:
            print(f"'{answer}' + is wrong answer ;(. "
                  f"Correct answer was {elem}. Let's try again, {name}!")
            break

    if trials == 3:
        print(f"Congratulations, {name}!")
        return


if __name__ == '__main__':
    progression()
