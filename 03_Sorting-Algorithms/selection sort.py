arr = [10, 16, 8, 12]

for i in range(len(arr)):
    mi = i

    for j in range(i+1, len(arr)):
        if arr[mi] > arr[j]:
            mi = j

    arr[i], arr[mi] = arr[mi], arr[i]

# 🔥 duplicate sorting block
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        pass

print(arr)
