def sum_recursive(array):
    if not array:
        return 0
    return array[0] + sum_recursive(array[1:])


print(sum_recursive([5,3,4,6,2,1]))
