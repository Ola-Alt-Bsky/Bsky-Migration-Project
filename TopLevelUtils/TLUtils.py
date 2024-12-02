# Base Libraries
import os
import re

import atproto_client.exceptions
# 3rd Party Libraries
from atproto import Client
from atproto_client.exceptions import BadRequestError

# Personal Libraries
from LoadingUtils import *


def sanitize_filepath(fp: str) -> str:
    # Normalize the path to remove redundant separators and up-level references
    safe_path = os.path.normpath(fp)

    # Confirms that the path only contains valid characters
    if not re.match(r'^(?:[A-Za-z]:)?[\w\-.\\/ ]+$', safe_path):
        raise ValueError("The path contains invalid characters.")

    # Convert to an absolute path
    abs_path = os.path.abspath(safe_path)

    # Ensure it's not a directory
    if os.path.isdir(abs_path):
        raise ValueError("The path is leads to a directory.")

    return abs_path


def import_accounts(fp: str) -> list:
    print('Importing file...')

    follow_list = None
    follow_format = None

    if not os.path.exists(fp):  # Check if filepath exists
        print("File doesn't exist. Please try again.")
    elif '.json' in fp:  # JSON files
        follow_list, follow_format = json_specific_loads(fp)
    elif '.txt' in fp:  # TXT files
        follow_list, follow_format = text_specific_loads(fp)
    else:
        print("Unsupported format. Please try again.")

    print('List:', follow_list)
    print('Format:', follow_format)

    return follow_list


def follow_account(c: Client, handle: str) -> int:
    # Lowercase everything
    handle = handle.lower()

    # Add ending if needed
    if '.bsky.social' not in handle:
        handle = handle + '.bsky.social'

    try:
        # Get did and follow
        did = c.get_profile(handle).did
        c.follow(did)
        print(handle, 'was sent a follow request.')
        return 1
    except BadRequestError:
        # Send message if error was not found
        print(handle, 'was not found.')
        return 0


def follow_all_accounts(account_list: list[str], usr: str, pwd: str) -> None:
    try:
        # Log into account
        client = Client()
        client.login(usr, pwd)

        # Loop through list
        total_count = 0
        follow_count = 0
        for username in account_list:
            total_count += 1
            follow_count += follow_account(client, username)

        # Do basic status
        print(follow_count, 'accounts were sent follow requests.')
        print(total_count - follow_count, 'accounts were not found.')
        print('Followed ratio of', follow_count/total_count)
    except atproto_client.exceptions.UnauthorizedError:
        print("Incorrect credentials were used. Try again.")
