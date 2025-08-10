arr = [[7, 8], [1, 5], [2, 4], [4, 6]]

# sort the array based on first element of the array
arr.sort()

# [[1, 5], [2, 4], [4, 6], [7, 8]]
output = []
output.append(arr[0])


for i in range(1, len(arr)):
    last = output[-1]
    curr = arr[i]

    if curr[0] <= last[1]:
        last[1] = max(last[1], curr[1])
    else:
        output.append(curr)

print(output)
