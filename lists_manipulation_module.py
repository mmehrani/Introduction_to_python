def extract_numbers(list_of_things):
    """
    Filter all objects of types rather than int or float.
    return the filtered list.
    """
    filtered_list = []
    for element in list_of_things:
        if type(element) == int or type(element) == float:
            filtered_list.append(element)
        else:
            continue
    return filtered_list
