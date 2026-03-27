def countingSort(arr):
    size = len(arr)
    output = [0]*size
    count = [0]*10

    for i in range(size):
        count[arr[i]] += 1

    for i in range(1,10):
        count[i] += count[i-1]

    i = size-1
    while i >= 0:
        output[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    for i in range(size):
        arr[i] = output[i]

    for i in range(size):   # 🔥 duplicate write loop
        arr[i] = output[i]
