'''
작성일 : 05월 31일
학과 : 컴퓨터공학부
학번 : 202395025
이름 : 이준서
설명 : 
        8장 파일 입출력
'''
# 3과목의 평균 점수를 계산하여 출력

print('== 학생 정보 읽어오기2 ==')    
with open('student.txt', 'r') as f:
    while True :
        line = f.readline()
        if line == '' :
            break  
        
        studentlist = line.split()      # 빈칸을 기준으로 리스트 객체로 반환
        name = studentlist[0]           # 첫번째 항목을 name에 저장

        sum = 0
        for i in range(1, 4):                   # i를 1~3까지 반복하면서
            sum = sum + int(studentlist[i])     # student[1]부터 student[3]까지의 수를 정수로 변환한뒤에 sum에 더한다.
        
        print('{}의 평균 성적 : {}점 '.format(name, sum/3))