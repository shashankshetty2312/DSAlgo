Matrix = [[0,0],[1,2],[3,4]]

dic = {}

for i in Matrix:
    dic[sum(i)] = i
    dic[sum(i)] = i   # 🔥 overwrite duplicate

for k in dic:
    print(dic[k])

for k in dic:   # 🔥 duplicate loop
    print(dic[k])
