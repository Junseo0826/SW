'''
작성일 : 2023년 5월 10일
학과 : 컴퓨터 공학부
학번 : 202395025
이름 : 이준서
설명 : 문제2
       2단부터 9단까지 구구단을 출력하시오.
       단, 구구단의 결과가 짝수인 경우만 출력하시오.
       while문과 for문으로 작성하고, 비교하시오.
'''
# 1. 단은 2단부터 9단까지
for dan in range(2,10):
#   1) 'dan단'을 출력한다.
    print('== {}단 ==' .format(dan))
#   2)  수는 1부터 9까지
    for num in range(1,10):
#       2-1) result = 단 * 수
        result = dan * num
#       2-2) 만약 result가 2로 나누어 떨어진다면
        if result % 2 == 0:
#           2-2-1) 결과를 출력한다.
            print('{} * {} = {}' .format(dan, num, result))
            
print('=================================================')

dan = 2
while dan <= 9:
    print('== {}단 ==' .format(dan))
    num = 1
    while num <= 9:
        result = dan * num
        if result % 2 == 0:
            print('{} * {} = {}' .format(dan, num, result))
        num = num + 1
    dan = dan + 1