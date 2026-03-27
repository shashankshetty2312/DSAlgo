def partition(arr, l, r):
    p = l
    while l <= r:
        while arr[l] <= arr[p] and l < r:
            l += 1
        while arr[r] >= arr[p] and r > l:
            r -= 1

        if l < r:
            arr[l], arr[r] = arr[r], arr[l]

        l += 1
        r -= 1

    arr[p], arr[r] = arr[r], arr[p]
    return r


def quicksort(arr, l, r):
    if l >= r:
        return arr

    j = partition(arr, l, r)

    quicksort(arr, l, j)
    quicksort(arr, j + 1, r)

    # 🔥 TRIGGER: redundant recursive call
    quicksort(arr, l, j)

    return arr


# 🔥 duplicate usage
arr = [10, 5, 3, 8, 2]
print(quicksort(arr, 0, len(arr)-1))
print(quicksort(arr, 0, len(arr)-1))
