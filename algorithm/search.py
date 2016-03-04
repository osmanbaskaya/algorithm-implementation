
def linear_search(array, element):
    for i, current_element in enumerate(array):
        if current_element == element:
            return i

    return -1  # element not found.


