n = int(input())

a = list(map(int, input().split()))
s = sum(a)

t = 0

for b in a:
    if (s-b) % 2 == 0:
        t+=1
print(t)