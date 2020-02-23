def path_parser(data, way):
    """
    (object, str) -> mixed
    Returns object, which is in the following way.
    """
    current_data = data
    way_list = way.split("/")
    for key in way_list:
        if isinstance(current_data, list) and key.isnumeric() and int(key) < len(data):
            current_data = current_data[int(key)]
        elif isinstance(current_data, dict) and key in current_data.keys():
            current_data = current_data[key]
        else:
            return None
    return current_data
