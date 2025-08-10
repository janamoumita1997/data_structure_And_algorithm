arr =[1,0,8,4,0,0,2,7,0,6,0]

a = 0
b = 0
while True:
    if b == len(arr)-1:
        break
    if arr[a] !=0 and arr[b]!= 0:
        a += 1
        b += 1
    elif arr[a] == 0 and arr [b] ==0:
        b += 1
    elif arr[a] == 0 and arr[b] !=0:
        temp = arr[b]
        arr[b] = arr[a]
        arr[a] = temp
        a += 1
        b += 1
print(arr)