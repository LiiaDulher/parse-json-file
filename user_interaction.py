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