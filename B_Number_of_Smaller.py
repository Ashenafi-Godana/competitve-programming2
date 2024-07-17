k, n = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
i = 0
c = [0] * len(b)
for j in range(len(b)):
    while i < len(a) and a[i] < b[j]:
        i+=1
    c[j] = i

print(*c)