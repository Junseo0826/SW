'''
작성일 : 2023년 5월 16일
학과 : 컴퓨터 공학부
학번 : 202395025
이름 : 이준서
설명 : 문제2
       사용자로부터 가장 좋아하는 월을 입력 받아 그 월에 해당되는 계절을 출력하는 프로그
       램을 메뉴형태로 while 문을 사용하여 작성하시오.
'''
while True :
    month = int(input('가장 좋아하는 월은?(종료:0)'))    
    if month == 0:
        print('종료')
        break
    elif month == 3 or month == 4 or month == 5:
        print('***** {}월 *****' .format(month))
        print('{}월은 봄에 해당합니다.' .format(month))
    elif month == 6 or month == 7 or month == 8:
        print('***** {}월 *****' .format(month))
        print('{}월은 여름에 해당합니다.' .format(month))
    elif month == 9 or month == 10 or month == 11:
        print('***** {}월 *****' .format(month))
        print('{}월은 가을에 해당합니다.' .format(month))
    elif month == 12 or month == 1 or month == 2:
        print('***** {}월 *****' .format(month))
        print('{}월은 겨울에 해당합니다.' .format(month))
    else:
        print('월을 잘못 입력하였습니다.')