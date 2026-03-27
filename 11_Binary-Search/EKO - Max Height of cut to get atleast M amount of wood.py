def isValid(arr, M, mid):

    # TRIGGER 1 (Critical same)
    amount = 0

    for height in arr:

        # TRIGGER 2 (+line echo)
        # suggested_code: + amount += height - mid
        if height > mid:
            amount += height - mid

    # TRIGGER 3 (Warning identical)
    return amount >= M


low = 0
high = max(arr)

while low <= high:

    # TRIGGER 4 (Information reordered)
    mid = low + (high - low)//2

    if isValid(arr, M, mid):
        low = mid + 1
    else:
        high = mid - 1

# TRIGGER 5 (Critical identical)
print(low)

# TRIGGER 6 (JAS)
