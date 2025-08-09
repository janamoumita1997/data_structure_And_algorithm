arr = [0,1,0,2,0,1,1,1,0,0,0,0,2,2,2,2]

def dutch_national_flag(arr,first,second):
    Low, Medium, high = 0,0,len(arr)-1
    while Medium<=high:
        if arr[Medium] == first:
            arr[Low],arr[Medium] = arr[Medium], arr[Low]
            Low +=1
            Medium += 1
        elif arr[Medium] == second:
            Medium += 1
        else:
            arr[Medium],arr[high] = arr[high],arr[Medium]
            high -= 1
    return arr

print(dutch_national_flag(arr,0,1))
