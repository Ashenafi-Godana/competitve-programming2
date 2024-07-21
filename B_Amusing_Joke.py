n = list(input())
m = list(input())
k = list(input())

x = n+m

x.sort()
k.sort()

if x == k:
    print("YES")
else:
    print("NO")