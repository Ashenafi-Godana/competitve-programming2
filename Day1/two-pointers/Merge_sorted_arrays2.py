# Merge Two sorted arrays using two pointers method
# O(n) runtime

a = [2, 3, 4, 5]
b = [6, 7, 8, 9]
c = [0] * (len(a) + len(b))
j = 0

i, j = 0, 0

while i < len(a) or j < len(b):
    if j == len(b) or i < len(a) and a[i] < b[j]:
        c[i+j] = a[i]
        i+=1
    else:
        c[i+j] = b[j]
        j+=1
print(c)

#  Runtime O(a.size() + b.size())
#  Space O(a.size() + b.size()  )