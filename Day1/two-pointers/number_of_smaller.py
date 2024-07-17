# Find how many smaller elements exist in a that are smaller than each element in b
# O(n) runtime
# O(1) Space
a = [1, 3, 5, 8, 10]
b = [2, 6, 7, 9, 13]
c = [0]*len(b)
i = 0
for j in range(len(b)):
    while i < len(a) and a[i] < b[j]:
        i+=1
    b[j] = i
print(b)
