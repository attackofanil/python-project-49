import prompt
import random
from random import randint

print('Welcome to the Brain Games!')
name = prompt.string('May I have your name? ')
print('Hello, ' + name + '!')
print('Answer "yes" if the number is even, otherwise answer "no".')

def main():
  index = 0
  while index <= 2:
    x = random.randint(1, 100)
    print('Question: ', x)
    answer = prompt.string('Your answer: ')
    result = 'Correct!'
    if (x % 2 == 0 and answer == 'yes') or (x % 2 != 0 and answer == 'no'):
      index += 1
      print(result)
    elif x % 2 == 0 and answer != 'yes' :
      print(f"'{answer}' + is wrong answer ;(. Correct answer was 'yes'. Let's try again, {name}!")
      break 
    elif x % 2 != 0 and answer != 'no':
      print(f"'{answer}' + is wrong answer ;(. Correct answer was 'no'. Let's try again, {name}!")
      break

    if index == 3:
      end = print(f"Congratulations, {name}!")
      return end


