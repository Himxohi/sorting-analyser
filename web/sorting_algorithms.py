import time

def bubble_sort(arr):
    n = len(arr)
    start = time.time()

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    end = time.time()
    return end - start


def selection_sort(arr):
    n = len(arr)
    start = time.time()

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    end = time.time()
    return end - start


def insertion_sort(arr):
    start = time.time()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

    end = time.time()
    return end - start


def merge_sort(arr):

    start = time.time()

    def merge(arr):
        if len(arr) > 1:

            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]

            merge(L)
            merge(R)

            i = j = k = 0

            while i < len(L) and j < len(R):

                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1

                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

    merge(arr)

    end = time.time()
    return end - start


def quick_sort(arr):

    start = time.time()

    def quick(arr):
        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr)//2]

        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return quick(left) + middle + quick(right)

    quick(arr)

    end = time.time()
    return end - start