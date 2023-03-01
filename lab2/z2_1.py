arr = [23, 17, 14, 6, 13, 10, 1, 5, 7, 12]


def check_if_max_heap(arr):
    for i in range(len(arr)):
        if 2*i+1 < len(arr) and arr[i] < arr[2*i+1]:
            return False
        if 2*i+2 < len(arr) and arr[i] < arr[2*i+2]:
            return False
    return True


print(check_if_max_heap(arr))
