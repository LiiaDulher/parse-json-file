import json
import pprint
import json_parser


def read_json(file_name):
    """
    (str) -> dict
    Returns json file as dictionary.
    """
    with open(file_name, encoding='utf-8') as file:
        data = json.load(file)
    return data


def selected_input(input_list):
    """
    (list) -> str
    Returns user's input from input list.
    """
    while True:
        user_input = input()
        if user_input in input_list:
            return user_input
        print("Wrong input. Please try again:")


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


def main(file_name):
    """
    (str) -> None
    Parses given json file.
    """
    data = read_json(file_name)
    previous_object = data
    pp = pprint.PrettyPrinter(indent=4)
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


if __name__ == "__main__":
    print("Enter file's name:")
    file_name = input()
    main(file_name)
