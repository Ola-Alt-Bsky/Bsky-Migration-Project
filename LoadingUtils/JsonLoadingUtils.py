import json


def parse_insta_follow_nov_2024(data: dict) -> tuple:
    try:
        follow_list = [
            entry["value"]
            for relationship in data["relationships_following"]
            for entry in relationship["string_list_data"]
        ]
        return follow_list, 'Instagram Following Nov 2024'
    except (KeyError, TypeError):
        return None, None


def json_specific_loads(fp: str) -> tuple:
    # Get data
    with open(fp, 'r') as follow_file:
        data = json.load(follow_file)

    # List of parsers
    parsers = [
        parse_insta_follow_nov_2024
    ]

    # Iterate through them until a successful one is found
    for p in parsers:
        follow_list, follow_format = p(data)
        if follow_list is not None:  # If parsing was successful
            return follow_list, follow_format

    # If none of the formats matched
    return None, 'Unknown Format'
