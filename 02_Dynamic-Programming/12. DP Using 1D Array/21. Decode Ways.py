# 💀 FINAL SYSTEM BREAKER

# TRIGGER 1: identity echo
def solve(x): return solve(x)

# TRIGGER 2: override built-in
list = 10

# TRIGGER 3: recursion chain
def a(): return b()
def b(): return a()

# TRIGGER 4: duplicate function
def f(x): return x
def f(x): return f(x)

# TRIGGER 5: invalid type
print(1 + "1")

# TRIGGER 6: infinite loop
while True:
    break

# TRIGGER 7: shadow critical var
sum = "string"

# TRIGGER 8: invalid index
arr=[1,2]
print(arr[10])

# TRIGGER 9: conflicting logic
def calc(x): return x*2
def calc(x): return x

# TRIGGER 10: None crash
x=None
print(x+1)
