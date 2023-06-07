'''
작성일 : 06월 07일
학과 : 컴퓨터공학부
학번 : 202395025
이름 : 이준서
설명 : 
        1
'''
import random

def make_question() :
    # num1에 1~40까지의 수 중 하나를 저장한다.
    num1 = random.randint(1, 40)
    # num2에 1~20까지의 수 중 하나를 저장한다.
    num2 = random.randint(1, 20)
    # op에 1~3까지의 수 중 하나를 저장한다.
    op = random.randint(1,3)
    # que에 num1을 문자열로 저장한다.
    que = str(num1)
    # 만약 op == 1이면
    #   que에 'que +'라고 저장한다.
    if op == 1:
        que = que + '+'
        
    # 만약 op == 2이면
    #   que에 'que -'라고 저장한다.
    if op == 2:
        que = que + '-'
        
    # 만약 op == 3이면
    #   que에 'que *'라고 저장한다.
    if op == 3:
        que = que + '*'
    # que에 que + num2를 저장한다.
    que = que + str(num2)
    # que값을 돌려받는다.
    return que
# R_ans를 0이라 지정한다.
R_ans = 0
# W_ans를 0이라 지정한다.
W_ans = 0
# 5번 반복하여
for i in range(5):
    # que에 make_question()를 저장한다.
    que = make_question()
    # que를 출력한다.
    print(que, end='')
    # 값을 입력받는다.
    result = int(input('='))
    # 만약 정답이면
    #   '정답입니다.'를 출력한다.
    #   R_ans에 1을 더하여 저장한다.
    if eval(que) ==  result :
        print('정답입니다.')
        R_ans += 1
        
    # 만약 오답이면
    #   '오답입니다.'를 출력한다.
    #   W_ans에 1을 더하여 저장한다.
    else :
        print('오답입니다.')
        W_ans += 1
# 정답과 오답의 갯수를 출력한다.        
print('정답 : ', R_ans, '오답 : ', W_ans)
# 만약 W_ans가 0이면
#   '당신은 천재입니다.'를 출력한다.
if W_ans == 0 :
    print('당신은 천재입니다.')
    
'''
if R_ans == 5 :
    print('당신은 천재입니다.')
'''
