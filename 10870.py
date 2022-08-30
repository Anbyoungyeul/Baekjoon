num = int(input())
num_arr = []
for i in range(num+1):
    if(i>1):
        num_arr.append(num_arr[i-1] + num_arr[i-2])
    else:
        num_arr.append(i)
print(num_arr[num])
