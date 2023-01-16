#!/usr/bin/env python3

from brain_game.scripts.brain_games import main
from brain_game.scripts.cli import welcome_user
from brain_game.game.calc import calc

main()
welcome_user()
calc()


if __name__ == '__main__':
    main()
    user_name = welcome_user()
    print(f"Hello, {user_name}!")

