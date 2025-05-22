# 자신의 MBTI를 입력하여 결과를 출력
from itertools import count

while True: # MBTI 입력을 틀리지 않고 입력했을 때 결과 출력 후 반복 종료
    user_input = input('MBTI를 입력하세요: ') # MBTI를 입력받기
    mbti = [] # MBTI를 한 글자씩 저장 ['I', 'N', 'F', 'J']
    energy_direction = '' # 에너지 방향
    perception = '' # 인식 기능
    decision = '' # 판단 기능
    life_style = '' # 생활 양식
    success = 0 # 유형 분석에 성공한 횟수

    for i in user_input: # 입력받은 MBTI를 한 글자씩 i에 저장
        mbti.append(i) # 리스트에 한 글자씩 저장

    if len(mbti) == 4: # 입력받은 MBTI가 4글자일 때(정상적으로 입력)
        if mbti[0] == 'e' or mbti[0] == 'E': # 입력한 첫번째 글자가 e 또는 E일 때
            energy_direction = '외향형'
            success += 1
        elif mbti[0] == 'i' or mbti[0] == 'I': # 입력한 첫번째 글자가 i 또는 I일 때
            energy_direction = '내향형'
            success += 1

        if mbti[1] == 's' or mbti[1] == 'S': # 입력한 첫번째 글자가 s또는 S일 때
            perception = '감각형'
            success += 1
        elif mbti[1] == 'n' or mbti[1] == 'N': # 입력한 첫번째 글자가 n 또는 N일 때
            perception = '직관형'
            success += 1

        if mbti[2] == 't' or mbti[2] == 'T' : # 입력한 첫번째 글자가 t 또는 T일 때
            decision = '사고형'
            success += 1
        elif mbti[2] == 'f' or mbti[2] == 'F': # 입력한 첫번째 글자가 f 또는 F일 때
            decision = '감정형'
            success += 1

        if mbti[3] == 'j' or mbti[3] == 'J': # 입력한 첫번째 글자가 j 또는 J일 때
            life_style = '계획적(판단형)'
            success += 1
        elif mbti[3] == 'p' or mbti[3] == 'P': # 입력한 첫번째 글자가 p 또는 P일 때
            life_style = '즉흥적(인식형)'
            success += 1

        if success == 4: # 4가지 유형 분석에 성공했을 때
            print('*** MBTI 분석결과 ***')
            print('당신은 ', energy_direction, '이고 ', perception, '이며 ', decision, '이며 ', life_style, '입니다.')
            break
        else: # MBTI 유형을 잘못입력함
            print('MBTI를 다시 입력해주세요.')
    else: # 입력받은 MBTI가 4글자가 아닐 때 (잘못 입력함)
        print('MBTI를 다시 입력해주세요.')
