#Baek-2501
"""
어떤 자연수 p와 q가 있을 때, 만일 p를 q로 나누었을 때 나머지가 0이면 q는 p의 약수이다.
그래서 6의 약수는 총 4개이다.
두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램 작성
(N의 약수의 개수가 K보다 적어서 약수가 존재하지 않을 경우 0 출력)
"""
try:
    first, second = map(int, input().split())
    result =[]
    for i in range(1, first+1):
        Div_first = first % i
        if Div_first == 0:
            result.append(i)
    if len(result) < second:
        print("0")
    else:
        print(result[second-1])   
except:
    print("1번째 숫자는 1이상 10000이하, 2번째 숫자는 1이상 n 이하 ")