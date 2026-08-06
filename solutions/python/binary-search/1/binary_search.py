def find(search_list, value):
    searching = search_list
    index_offset = 0
    while searching:
        middle = len(searching) // 2
        if searching[middle] == value:
            return index_offset + middle
        if searching[middle] < value:
            index_offset += middle + 1
            searching = searching[middle + 1:]
        else:
            searching = searching[:middle]
    raise ValueError("value not in array")
        