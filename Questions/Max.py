def recursive_max(array,i  = 0):
    if not array:
        raise ValueError("Array is empty")
    if i == len(array) - 1:
        return array[i]
    sub_max = recursive_max(array,i+1)
    return array[i] if array[i] > sub_max else sub_max

print(recursive_max([5,3,4,6,2,1]))