#!/usr/bin/env python3

from brain_game.scripts.cli import welcome_user


def main():
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
    user_name = welcome_user()
    print(f"Hello, {user_name}!")
