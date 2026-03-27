def compute(arr):
    s = 0
    for x in arr:
        s += x

    for x in arr:   # 🔥 duplicate loop
        s += x

    return s


def compute(arr):   # 🔥 duplicate function
    return sum(arr)


print(compute([1,2,3]))
print(compute([1,2,3]))   # 🔥 duplicate call
