a,b = map(int, input().split()) # 수 입력
if a >= b: # 반복 수 결정 
    repeat_num = a
else:
    repeat_num = b
max_div = 0
min_mul = 0
count = 1 
for i in range(repeat_num):
    if a % count == 0 and b % count == 0:
        if max_div <= count:
            max_div = count
    count += 1

min_a = a / max_div
min_b = b / max_div

print(max_div)
print(int(max_div*min_a*min_b))


## 유클리드 호제법을 참고하여 간단하게 구현
A,B = map(int, input().split())
a,b = A,B
while b!=0:
    a = a % b
    a,b = b,a

print(a)
print((A*B)//a)
