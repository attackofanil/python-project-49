import prompt
import random
from random import randint


def calc():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('What is the result of the expression?')
    index = 0
    while index < 3:
        x = random.randint(50, 100)
        y = random.randint(1, 50)
        z = ['+', '-', '*']
        end = z[randint(0, len(z)-1)]
        print(f"Question: {x} {end} {y}")
        if end == '+':
          total = x + y
        elif end == '-':
          total = x - y
        elif end == '*':
          total = x * y
        answer = int(input('Your answer: '))
        result = 'Correct!'
        if answer == total:
          index += 1
          print(result)
        elif answer != total:
          print(f"'{answer}' + is wrong answer ;(.\
 Correct answer was {total}. Let's try again, {name}!")
          break
    if index == 3:
       end = print(f"Congratulations, {name}!")
       return end
