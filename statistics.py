def median(lists_of_coordinates):
    sorted_list = sorted(lists_of_coordinates)
    center_index = int(len(lists_of_coordinates) / 2)
    if len(lists_of_coordinates) % 2 == 0:
        result = (sorted_list[center_index] + sorted_list[center_index - 1]) / 2
    else:
        # Now we need only 1 index for exact value
        result = sorted_list[center_index]

    return result