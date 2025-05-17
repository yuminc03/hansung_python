# 자신의 MBTI를 입력하여 결과를 출력
from itertools import count

while True: # MBTI 입력을 틀리지 않고 입력했을 때 반복 종료
    user_input = input('MBTI를 입력하세요: ')
    mbti = []
    energy_direction = '' # 에너지 방향
    perception = '' # 인식 기능
    decision = '' # 판단 기능
    life_style = '' # 생활 양식
    success = 0

    for i in user_input:
        mbti.append(i)

    if len(mbti) == 4:
        if mbti[0] == 'e' or mbti[0] == 'E':
            energy_direction = '외향형'
            success += 1
        elif mbti[0] == 'i' or mbti[0] == 'I':
            energy_direction = '내향형'
            success += 1

        if mbti[1] == 's' or mbti[1] == 'S':
            perception = '감각형'
            success += 1
        elif mbti[1] == 'n' or mbti[1] == 'N':
            perception = '직관형'
            success += 1

        if mbti[2] == 't' or mbti[2] == 'T':
            decision = '사고형'
            success += 1
        elif mbti[2] == 'f' or mbti[2] == 'F':
            decision = '감정형'
            success += 1

        if mbti[3] == 'j' or mbti[3] == 'J':
            life_style = '계획적(판단형)'
            success += 1
        elif mbti[3] == 'p' or mbti[3] == 'P':
            life_style = '즉흥적(인식형)'
            success += 1

        if success == 4:
            print('*** MBTI 분석결과 ***')
            print('당신은 ', energy_direction, '이고 ', perception, '이며 ', decision, '이며 ', life_style, '입니다.')
            break
        else:
            print('MBTI를 다시 입력해주세요.')
    else:
        print('MBTI를 다시 입력해주세요.')
