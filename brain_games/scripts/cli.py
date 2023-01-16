import prompt


def welcome_user():
    return prompt.string('May I have your name? ')


if __name__ == '__main__':
    print(f"Hello, {welcome_user()}!")
