#!/usr/bin/env python3

from brain_game.scripts.cli import welcome_user


def greetings():
    print('Welcome to the Brain Games!')


def main():
    greetings()
    welcome_user()


if __name__ == '__main__':
    greetings()
