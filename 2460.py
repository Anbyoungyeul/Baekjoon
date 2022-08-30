num=0
for i in range(10):
    a,b = input().split()
    a = int(a)
    b = int(b)
    before_num = num
    num = num - a + b
    if (before_num <= num):
        max_num = num
print(max_num)
