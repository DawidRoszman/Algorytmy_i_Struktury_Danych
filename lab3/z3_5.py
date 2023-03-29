from timeit import default_timer as timer
from random import randint
import sys

sys.setrecursionlimit(1000000)


def modified_quick_sort(A, p, r, c):
    if p < r:
        if r-p+1 < c:
            A[p:r+1] = bubble_sort(A[p:r+1])
        else:
            q = partition(A, p, r)
            modified_quick_sort(A, p, q, c)
            modified_quick_sort(A, q+1, r, c)


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q)
        quick_sort(A, q+1, r)


def partition(A, p, r):
    x = A[r]  # element wyznaczajacy podział
    i = p-1
    for j in range(p, r+1):
        if A[j] <= x:
            i = i+1
            A[i], A[j] = A[j], A[i]
    if i < r:
        return i
    else:
        return i-1


def bubble_sort(A):
    for i in range(len(A)):
        for j in range(len(A)-1, i, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
    return A


def measure_modified_quick_sort(A, c):
    start = timer()
    modified_quick_sort(A, 0, len(A)-1, c)
    stop = timer()
    return stop-start


def measure_quick_sort(A):
    start = timer()
    quick_sort(A, 0, len(A)-1)
    stop = timer()
    return stop - start


if __name__ == "__main__":
    x = 10
    list_of_arr = [
            [randint(1, x) for _ in range(
                x**i if x**i < 10_000 else 10_000)] for i in range(10)
    ]
    list_of_arr.append([i for i in range(1, x+1)])
    testing_arr = [2, 8, 1, 3, 5, 4, 7, 6, 10, 9]
    sorted_testing_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    modified_quick_sort(testing_arr, 0, len(testing_arr)-1, 5)
    # Testuje czy ręcznie posortowana lista
    # jest taka sama jak posortowana przez quicksort
    print(testing_arr == sorted_testing_arr)

    with open("wyniki.txt", "w") as f:
        for arr in list_of_arr:
            # print(f"Array: {arr}")
            time1 = measure_modified_quick_sort(arr, 5)
            time2 = measure_quick_sort(arr)
            if arr == list_of_arr[-1]:
                print("Worst case scenario")
                f.write("Worst case scenario\n")
            print("Length of array", len(arr))
            print(f"Modified quick sort time: {time1}")
            print(f"Quick sort time: {time2}")
            print("\n\n------------------------\n\n")
            f.write(f"Length of array: {len(arr)}\n")
            f.write(f"Modified quick sort time: {time1}\n")
            f.write(f"Quick sort time: {time2}\n")
            f.write("\n\n------------------------\n\n")
