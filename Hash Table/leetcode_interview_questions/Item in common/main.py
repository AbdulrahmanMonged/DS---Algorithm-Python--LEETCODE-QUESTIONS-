def item_in_common(list1, list2):
    data_map = {}
    for item in list1:
        data_map[item] = True
    for item in list2:
        if data_map.get(item, None):
            return True
    return False


list1 = [1, 3, 5]
list2 = [2, 4, 5]


print(item_in_common(list1, list2))


"""
    EXPECTED OUTPUT:
    ----------------
    True

"""
