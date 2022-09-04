a,b = map(int, input().split()) # 수 입력
if a >= b:
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
