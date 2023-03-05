def heapify_iter(A, heapSize, i):
    while True:
        left = 2*i+1  # lewy syn
        right = 2*i+2  # prawy syn
        if left < heapSize and A[left] > A[i]:
            largest = left
        else:
            largest = i
        if right < heapSize and A[right] > A[largest]:
            largest = right
        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            i = largest
        else:
            break
    return A


def buildHeap(A):
    heapSize = len(A)
    k = int((len(A)-2)/2)
    # k - ojciec ostatniego węzła
    for i in range(k, -1, -1):
        heapify_iter(A, heapSize, i)
    return A


def heapSort(A):
    A = buildHeap(A)
    heapSize = len(A)
    for i in range(len(A)-1, 0, -1):
        A[0], A[heapSize-1] = A[heapSize-1], A[0]
        heapSize -= 1
        heapify_iter(A, heapSize, 0)
    return A


with open('data.txt', 'r') as f:
    lines = f.read().splitlines()
    data = [int(x) for x in lines]


with open('wyniki_iter.txt', 'w') as f:
    f.write('Wyniki iteracyjnie ' + str(heapSort(data)))
