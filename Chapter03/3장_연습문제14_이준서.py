'''
작성일 : 2023년 4월 4일
학과 : 컴퓨터 공학부
학번 : 202395025
이름 : 이준서
설명 : 연습문제 14
       5과목의 점수를 입력 받아 총점과 평균을 구하는 프로그램을 작성하시오.
'''
# 1. 국어 점수를 정수로 변환하여 score 1에 저장
score_1 = int(input('국어 점수 :'))
# 2. 수학 점수를 정수로 변환하여 score 2에 저장
score_2 = int(input('수학 점수 :'))
# 3. 영어 점수를 정수로 변환하여 score 3에 저장
score_3 = int(input('영어 점수 :'))
# 4. 사회 점수를 정수로 변환하여 score 4에 저장
score_4 = int(input('사회 점수 :'))
# 5. 과학 점수를 정수로 변환하여 score 5에 저장
score_5 = int(input('과학 점수 :'))
# 6. 총점 계산
sum = score_1 + score_2 + score_3 + score_4 + score_5
# 7. 평균 계산
avg = sum / 5
# 8. 총점과 평균 출력
print('국어 점수 : {} 수학 점수 : {} 영어 점수 : {} 사회 점수 : {} 과학점수 : {}' .format(score_1, score_2, score_3, score_4, score_5))
print('총점은 {} 입니다. 평균은 {:.2f} 입니다.' .format(sum, avg))