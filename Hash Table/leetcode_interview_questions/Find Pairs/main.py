def find_pairs(arr1, arr2, target):
    result_set = set()
    for m in arr1:
        complement = target - m
        if complement in arr2:
            result_set.add((m, complement))
    return list(result_set)
        




arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""