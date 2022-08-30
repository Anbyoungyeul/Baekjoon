num = []
before_num =0
for i in range(10):
    a,b = input().split()
    a = int(a)
    b = int(b)
    before_num = before_num - a + b
    num.append(before_num)
print(max(num))
