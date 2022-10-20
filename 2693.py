count = int(input()) # 입력 받을 배열의 개수
for i in range(count):
    input_array = list(map(int, input().split())) # 리스트 입력 받기(공백 기준 분리)
    input_array.sort()
    print(input_array[7]) # 뒤에서 2번째 출력
