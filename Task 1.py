N = int(input())
lst = [i for i in range(2, N+1)]
p = lst[0]
for l in lst:
    for i in lst:
        for j in range(2, N):
            if i == p*j:
                lst.remove(i)
    p = l
print(lst)