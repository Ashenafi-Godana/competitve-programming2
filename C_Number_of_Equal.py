n, k = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

i = 0
res = 0
count = 0
k = 0
for j in range(len(arr2)):
    count = 0
    k+=1
    while i < len(arr1) and arr2[j] == arr1[i]:
        res+=1
        count+=1
        i+=1
        print("counted" + str(i) + " = " + str(res))
    
    if j < len(arr2)-1 and arr2[j] == arr2[j+1]:
        res+=count
        print("counted the same" + str(count) + " = " + str(res))

print(res)