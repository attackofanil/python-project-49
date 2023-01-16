#!/usr/bin/env python3

from brain_game.scripts.brain_games import main
from brain_game.game.brain_even import even
from brain_game.scripts.cli import welcome_user

main()
even()


if __name__ == '__main__':
    user_name = welcome_user()
    print(f"Hello, {user_name}!")
    main()
    even()
