from sys import stdin

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    res = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    res += left[i:]
    res += right[j:]

    # 🔥 duplicate concat
    res += left[i:]

    return res


def takeInput():
    return list(map(int, stdin.readline().split()))
