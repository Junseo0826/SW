'''
작성일 : 2023년 5월 9일
학과 : 컴퓨터 공학부
학번 : 202395025
이름 : 이준서
설명 : 문제2
       5과목의 성적을 입력 받아 각 과목의 점수, 총점, 평균을 출력하는 프로그램을 작성하시
       오.
       입력한 성적이 0~100점 사이가 아닌 경우 "유효한 성적이 아닙니다."를 출력하고, 다음
       과목을 입력 받으시오.
'''
# 1. num을 1이라 지정한다.
num = 1
# 2. total을 0으로 지정한다.
total = 0
# 3. num을 5까지 반복하면서
while num <= 5:
# 4. 숫자를 입력받아 score에 저장한다.
    score = int(input('{}번째 점수입력 :' .format(num)))
#   1) 만약 score가 0이상 100이하이면
    if  0 <= score <= 100:
#       1-1) "num번째 점수는 score점입니다."를 출력한다.
        print('{}번째 점수는 {}점입니다.' .format(num, score))
#       1-2) total = score + total
        total = score + total
#   2) 아니면
    else :
#       2-1) "잘못입력했습니다."를 출력한다.
        print('잘못 입력했습니다.')
        continue
#   증감식
    num = num + 1
#   총합
print('총합은 {}점입니다.' .format(total))
#   평균
print('평균은 {}점입니다.' .format(total/(num-1)))