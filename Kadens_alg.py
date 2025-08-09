# find the largest su array having max sum.
'''
1. Either extend the array 
    if sub_arr + current > current
2. start the ne array
    if sub_arr + current < current

if 
sub_arr  -> +ve, current -> +ve => extend
sub_arr  -> +ve, current -> -ve => extend
sub_arr  -> -ve, current -> +ve => new
sub_arr  -> -ve, current -> -ve => new
'''

arr = [-11,-2,-3,-1,-2,-5]
current = arr[0]
max_global = arr[0]

for i in range(1,len(arr)):
    current = max(current+arr[i],arr[i])
    if current> max_global:
        max_global = current
print(max_global)