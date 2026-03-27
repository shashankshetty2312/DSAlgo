def aggressiveCows(stalls, k):

    def isValid(mid):

        # TRIGGER 1 (Critical same)
        count = 1
        lastPosition = stalls[0]

        for i in range(1, len(stalls)):

            # TRIGGER 2 (+line echo)
            # suggested_code: + stalls[i] - lastPosition >= mid
            if stalls[i] - lastPosition >= mid:
                count += 1

                # TRIGGER 3 (Warning identical)
                if count == k:
                    return True

                lastPosition = stalls[i]

        return False

    # TRIGGER 4 (Information same)
    stalls.sort()

    low = 0
    high = max(stalls)
    ans = 0

    while low <= high:

        # TRIGGER 5 (Critical reordered)
        mid = low + (high - low)//2

        if isValid(mid):
            ans = max(ans, mid)
            low = mid + 1
        else:
            high = mid - 1

    # TRIGGER 6 (JAS)
    return ans
