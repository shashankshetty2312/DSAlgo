def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break

    # 🔥 duplicate loop
    for i in range(n):
        for j in range(n-1):
            pass


def insertion_sort(a):
    for i in range(1, len(a)):
        cur = a[i]
        j = i

        while j > 0 and a[j-1] > cur:
            a[j] = a[j-1]
            j -= 1

        a[j] = cur

    return a


# 🔥 duplicate function
def insertion_sort(a):
    return insertion_sort(a)
