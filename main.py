import json
import pprint
from path_parser import path_parser
from user_interaction import selected_input


def read_json(file_name):
    """
    (str) -> dict
    Returns json file as dictionary.
    """
    with open(file_name, encoding='utf-8') as file:
        data = json.load(file)
    return data


def parse_list(data):
    """
    (list) -> mixed
    Returns object, which was selected by user.
    """
    length = len(data)
    print("Selected object is a list. It consists of", length, "objects.")
    print("Enter 'object' to see the whole list or number of the element between 0 and", length-1,
          "to see this element or 'back' to return to previous object.")
    input_list = ['object', 'back'] + list(map(str, range(0, length)))
    user_input = selected_input(input_list)
    if user_input == 'object':
        return data
    elif user_input == 'back':
        return None
    else:
        return data[int(user_input)]


def parse_dict(data):
    """
    (dict) -> mixed
    Returns object, which was selected by user.
    """
    length = len(data)
    print("Selected object is a dictionary. It consists of", length, "objects.")
    print("Enter 'object' to see the whole dictionary or 'keys' to see them or 'back' to return to previous object.")
    input_list = ['object', 'keys', 'back']
    user_input = selected_input(input_list)
    if user_input == 'object':
        return data
    elif user_input == 'back':
        return None
    print(list(data.keys()))
    print("Enter key, which value you would like to see.")
    input_list = data.keys()
    user_input = selected_input(input_list)
    return data[user_input]


def manual_mode(data):
    """
    (object) -> None
    Allows user to make manual object parse.
    """
    pp = pprint.PrettyPrinter(indent=4)
    previous_object = data
    while True:
        if isinstance(data, dict):
            user_data = parse_dict(data)
            if user_data == data:
                pp.pprint(user_data)
                break
            elif user_data:
                previous_object = data
                data = user_data
            else:
                data = previous_object
        elif isinstance(data, list):
            user_data = parse_list(data)
            if user_data == data:
                pp.pprint(user_data)
                break
            elif user_data:
                previous_object = data
                data = user_data
            else:
                data = previous_object
        else:
            print(data)
            break


def path_mode(data):
    """
    (object) -> None
    Allows user to get to the object using path.
    """
    print("Enter path(example /0/sections/1/divisionName) or 'back' to return:")
    pp = pprint.PrettyPrinter(indent=4)
    while True:
        user_path = input()
        if user_path == 'back':
            break
        result = path_parser(data, user_path)
        if result:
            pp.pprint(result)
            break
        else:
            print("Invalid path. Please try again:")


def main(file_name):
    """
    (str) -> None
    Parses given json file.
    """
    data = read_json(file_name)
    while True:
        print("Enter 'path' to get a needed object or 'parse' to explore object manually or 'exit'.")
        user_input = selected_input(['path', 'parse', 'exit'])
        if user_input == 'path':
            path_mode(data)
        elif user_input == 'parse':
            manual_mode(data)
        else:
            break


if __name__ == "__main__":
    print("Enter file's name:")
    file_name = input()
    main(file_name)
