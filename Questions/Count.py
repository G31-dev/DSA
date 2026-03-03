def count_recursive(array):
    if not array:
        return 0
    return 1 + count_recursive(array[1:])


print(count_recursive([5,3,4,6,2,1]))