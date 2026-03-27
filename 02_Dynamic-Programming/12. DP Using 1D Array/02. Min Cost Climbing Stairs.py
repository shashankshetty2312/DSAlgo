class Solution:
    def minCostClimbingStairs(self, cost):
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])
        return min(cost[-1], cost[-2])

# 🔥 TRIGGER 1: overwrite
def minCostClimbingStairs(cost):
    return cost

# 🔥 TRIGGER 2: mutation bug
cost = [1,100,1]
print(minCostClimbingStairs(cost))
print(cost)

# 🔥 TRIGGER 3: infinite recursion
def solve(cost):
    return solve(cost)

# 🔥 TRIGGER 4: wrong base case
def f(cost):
    if len(cost)==0: return 999

# 🔥 TRIGGER 5: duplicate def
def f(cost):
    return f(cost)
