import random
import prompt
from brain_game.scripts.cli import welcome_user


def progression():
    user_name = welcome_user()
    print('What number is missing in the progression?')
    i = 0
    while i < 3:
        sequence = list(range(random.randint(0, 10), random.randint(80, 100), random.randint(2, 10))[0:10])
        find_elem = str(random.choices(sequence, k=1))
        elem = int(find_elem[1:-1])
        index_elem = sequence.index(elem)
        sequence.pop(index_elem)
        str(sequence.insert(index_elem, '..'))
        print('Question: ' + " ".join(map(str, sequence)))
        answer = prompt.string('Your answer: ')
        result = 'Correct!'
        if answer == str(elem):
            i += 1
            print(result)
        elif answer != elem:
            print(f"'{answer}' + is wrong answer ;(. "
                  f"Correct answer was {elem}. Let's try again, {user_name}!")
            break

    if i == 3:
        print(f"Congratulations, {user_name}!")
        return


if __name__ == '__main__':
    progression()
