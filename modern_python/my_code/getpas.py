from getpass import getpass

def create_user():
    username = input('Enter username: ')
    password = getpass('Enter password: ')
    print(username, password)

create_user()

