

def welcome_user():
    user_name = input('May I have your name? ')
    return user_name
    print(f"Hello, {user_name}!")


if __name__ == '__main__':
    user_name = welcome_user()
    print(f"Hello, {user_name}!")
