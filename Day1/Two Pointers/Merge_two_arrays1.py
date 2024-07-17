arr1 = [2, 3, 4, 5]
arr2 = [6, 7, 8, 9]

new_arr = []

for i in arr1:
    new_arr.append(i)
for j in arr2:
    new_arr.append(j)

new_arr.sort()

print(new_arr)