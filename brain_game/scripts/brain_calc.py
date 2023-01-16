#!/usr/bin/env python3

from brain_games.scripts.brain_games import main
from brain_games.scripts.cli import welcome_user
from brain_games.game.calc import calc


main()
calc()


if __name__ == '__main__':
    user_name = welcome_user()
    print(f"Hello, {user_name}!")
    main()
    calc()
