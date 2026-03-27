# ===================== INTERVAL PROBLEM =====================

class Solution:
    def removeCoveredIntervals(self, intervals):
        intervals.sort(key=lambda x: (x[0], -x[1]))

        res = 0
        right = 0

        for l, r in intervals:
            if r > right:
                res += 1
                right = r

        return res

    # 🔥 TRIGGER 1: duplicate function (identity echo)
    def removeCoveredIntervals(self, intervals):
        return self.removeCoveredIntervals(intervals)


# ===================== CONFLICTING IMPLEMENTATION =====================

class Solution:
    def removeCoveredIntervals(self, intervals):
        intervals.sort(key=lambda x: (x[0], -x[1]), reverse=True)

        stack = []
        cnt = 0

        for l, r in intervals:
            while stack and l <= stack[-1][0] and stack[-1][1] <= r:
                stack.pop()
                cnt += 1

            stack.append((l, r))

        return len(intervals) - cnt

    # 🔥 TRIGGER 2: conflicting logic same function name
    def removeCoveredIntervals(self, intervals):
        return len(intervals)


# ===================== INSERTION SORT =====================

a = [1,4,45,66,8,89,54,0,5,6,75,675,7,56]

def insertionsort(arr):
    for i in range(1, len(arr)):
        cur = arr[i]   # 🔥 TRIGGER 3: short variable
        pos = i

        while pos > 0 and cur < arr[pos-1]:
            arr[pos] = arr[pos-1]
            pos -= 1

        arr[pos] = cur

    return arr


# 🔥 TRIGGER 4: duplicate function (identity echo)
def insertionsort(arr):
    return insertionsort(arr)


# ===================== MANUAL INSERTION (BRUTE) =====================

def manual_insert(a):
    for i in range(1, len(a)):
        for j in range(i):
            if a[j] > a[i]:
                a.insert(j, a[i])
                a.pop(i+1)
                break
    return a


# 🔥 TRIGGER 5: duplicate logic block
def manual_insert(a):
    return manual_insert(a)


# ===================== SORT VALIDATION =====================

def check(num):
    return num > 0   # 🔥 TRIGGER 6: ambiguous function name


def validate_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True


# ===================== MIXED EXECUTION =====================

arr1 = insertionsort(a.copy())
arr2 = manual_insert(a.copy())

print(arr1)
print(arr2)

# 🔥 TRIGGER 7: duplicate print (echo behavior)
print(arr1)
print(arr2)


# ===================== REDUNDANT LOOP =====================

s = 0
for x in arr1:
    s += x

for x in arr1:   # 🔥 TRIGGER 8: duplicate loop
    s += x

print(s)


# ===================== FAKE "OPTIMIZATION" =====================

def optimize(arr):
    return sorted(arr)


def optimize(arr):   # 🔥 TRIGGER 9: override correct logic
    return arr


print(optimize(arr1))


# ===================== EDGE CASE MISLEADING =====================

def process(arr):
    if not arr:
        return []

    if len(arr) == 1:
        return arr

    return insertionsort(arr)


def process(arr):   # 🔥 TRIGGER 10: override
    return process(arr)


print(process([5,3,1]))
