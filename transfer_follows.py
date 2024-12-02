from TopLevelUtils import *


def print_introduction():
    print('Welcome to the follower transfer program! Created by me, Ola-Alt.')
    print('I like following art and I amassed way too many follows to bother going one by one.')
    print('So instead I spent a few days writing a Python program with as little effort as possible!')
    print('As far as I know, the best way to do it is to just get an archive of your data, and go from there.')
    print("This program's purpose is that once you have that file where your followers are kept, it will do the rest.")
    print('All you will need to do is type the filepath of the file into here and it will parse through the file for you.')
    print('With that said, hope I made your transition to bsky easier!\n')


def print_support():
    print('Last updated: November 2024')
    print('This program supports the following:')
    print('Instagram JSON')
    print('\nTo add support, please let me know at @ola-alt.bsky.social. Or fork the project on github.\n')


def get_credentials() -> tuple[str, str]:
    print('\nList created!')
    print('Next, you will enter your bsky handle and password.')
    print('This program will only use this code to authenticate the API and nothing more.\n')

    user_handle = input('Please enter your bsky handle (i.e. user.bsky.social): ')
    password = input('Please enter your bsky password: ')

    return user_handle, password


if __name__ == '__main__':
    # Intro text
    print_introduction()
    print_support()

    # Prompt user
    filepath = input('Enter the filepath of your file: ')

    # Clean filepath input
    filepath = sanitize_filepath(filepath)

    # Import accounts
    account_list = import_accounts(filepath)

    if account_list is not None:
        usr, pwd = get_credentials()

        # Log into account and start following
        follow_all_accounts(account_list, usr, pwd)
