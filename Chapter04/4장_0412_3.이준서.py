'''
작성일 : 2023년 4월 11일
학과 : 컴퓨터 공학부
학번 : 202395025
이름 : 이준서
설명 : 두 개의 숫자를 입력 받아 두 숫자가 모두 짝수이면 " 두 숫자가 모두 짝수입니다."를 출
        력하고, 모두 홀수이면 "두 숫자가 모두 홀수입니다."를 출력하고, 그렇지 않으면 "짝수와
        홀수가 섞여 있습니다."를 출력하는 프로그램을 작성하시오.
'''
# 1. 입력받은 점수를 정수로 변환하여 점수 변수 score에 저장한다.
score = int(input('점수 입력 :'))
# 2. 만약에 90 <= score <= 100 이면
#       1) "A학점 입니다."를 출력한다.
if 90 <= score <= 100 :
    print('A학점 입니다.')
# 3. 아니고 만약에 80 <= score <= 89 이면
#       1) "B학점 입니다."를 출력한다.
elif 80 <= score <= 89 :
    print('B학점 입니다.')
# 4. 아니고 만약에 70 <= score <= 79 이면
#       1) "C학점 입니다."를 출력한다.
elif 70 <= score <= 79 :
    print('C학점 입니다.')
# 5. 아니고 만약에 60 <= score <= 69 이면
#       1) "D학점 입니다."를 출력한다.
elif 60 <= score <= 69 :
    print('D학점 입니다.')
# 6. 아니면
#       1) "F학점 입니다."를 출력한다.
else :
    print('F학점 입니다.')