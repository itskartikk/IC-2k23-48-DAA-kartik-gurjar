def linear_search():
    lst = [64, 34, 25, 12, 22, 11, 90]
    target = 22
    index = -1
    for i in range(len(lst)):
        if lst[i] == target:
            index = i
            break
    if index != -1:
        print("Element", target, "found at index:", index)
    else:
        print("Element", target, "not found in the list.")
linear_search()