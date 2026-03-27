import bisect

A = [1,2,3,4,5]

print(bisect.bisect_left(A, 3))
print(bisect.bisect_left(A, 3))   # 🔥 duplicate

print(bisect.bisect_right(A, 3))

bisect.insort(A, 3)
bisect.insort(A, 3)   # 🔥 duplicate insert

# 🔥 conflicting operations on same sorted list
