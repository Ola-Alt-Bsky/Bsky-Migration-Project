def parse_old_twitter_scuffed_nov_2024(lines: list) -> tuple:
    # Strip newline characters from each line
    stripped_lines = [line.strip() for line in lines]

    # Check format to make sure it's the right one
    try:
        search_check = stripped_lines[1] == 'Search Twitter'
        tweet_check = stripped_lines[3] == 'Tweet'
        follow_check = stripped_lines[11] == 'Following'

        # Filter handles out
        follow_list: list[str] = [line for line in stripped_lines if line.startswith('@')]

        # One more check
        handle_check = follow_list[0] == follow_list[1]
    except IndexError:
        print("List was not long enough to analyze. Try again")
        return None, None

    # Only return the list if the format for this is correct
    if follow_list and search_check and tweet_check and follow_check and handle_check:
        # Pop your own handle
        follow_list.pop(0)
        follow_list.pop(0)

        # Get rid of @ symbol
        follow_list = [handle.replace('@', '') for handle in follow_list]

        return follow_list, 'Old Twitter Scuffed Following Nov 2024'
    else:
        return None, None


def text_specific_loads(fp: str) -> tuple:
    # Open the file in read mode
    with open(fp, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()

    # List of parsers
    parsers = [
        parse_old_twitter_scuffed_nov_2024
    ]

    # Iterate through them until a successful one is found
    for p in parsers:
        follow_list, follow_format = p(lines)
        if follow_list is not None:  # If parsing was successful
            return follow_list, follow_format

    # If none of the formats matched
    return None, 'Unknown Format'
