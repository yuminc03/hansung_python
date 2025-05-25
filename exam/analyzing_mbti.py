# 자신의 MBTI를 입력하여 결과를 출력
energy_direction = '' # 에너지 방향
perception = '' # 인식 기능
decision = '' # 판단 기능
life_style = '' # 생활 양식

while True: # MBTI 입력을 틀리지 않고 입력했을 때 결과 출력 후 반복 종료
    print("*** MBTI 분석 ***")
    energy_input = input('당신은 E인지 I인지 입력하세요: ')
    percept_input = input('당신은 S인지 N인지 입력하세요: ')
    dec_input = input('당신은 T인지 F인지 입력하세요: ')
    life_style_input = input('당신은 J인지 P인지 입력하세요: ')
    success = 0 # 유형 분석에 성공한 횟수 (성공 횟수가 4일 때 분석 성공함)

    if energy_input == 'e' or energy_input == 'E': # 입력한 첫번째 글자가 e 또는 E일 때
        energy_direction = '외향형' # 에너지 방향 = '외향형'
        success += 1 # 성공 횟수 1 증가
    elif energy_input == 'i' or energy_input == 'I': # 입력한 첫번째 글자가 i 또는 I일 때
        energy_direction = '내향형' # 에너지 방향 = '내향형'
        success += 1 # 성공 횟수 1 증가

    if percept_input == 's' or percept_input == 'S': # 입력한 첫번째 글자가 s또는 S일 때
        perception = '감각형' # 인식 기능 = '감각형'
        success += 1 # 성공 횟수 1 증가
    elif percept_input == 'n' or percept_input == 'N': # 입력한 첫번째 글자가 n 또는 N일 때
        perception = '직관형' # 인식 기능 = '직관형'
        success += 1 # 성공 횟수 1 증가

    if dec_input == 't' or dec_input == 'T' : # 입력한 첫번째 글자가 t 또는 T일 때
        decision = '사고형' # 판단 기능 = '사고형'
        success += 1 # 성공 횟수 1 증가
    elif dec_input == 'f' or dec_input == 'F': # 입력한 첫번째 글자가 f 또는 F일 때
        decision = '감정형' # 판단 기능 = '감정형'
        success += 1 # 성공 횟수 1 증가

    if life_style_input == 'j' or life_style_input == 'J': # 입력한 첫번째 글자가 j 또는 J일 때
        life_style = '계획적(판단형)' # 생활 양식 = '계획적'
        success += 1 # 성공 횟수 1 증가
    elif life_style_input == 'p' or life_style_input == 'P': # 입력한 첫번째 글자가 p 또는 P일 때
        life_style = '즉흥적(인식형)' # 생활 양식 = '즉흥적'
        success += 1 # 성공 횟수 1 증가

    if success == 4: # 4가지 유형 분석에 성공했을 때
        print('*** MBTI 분석결과 ***')
        print('당신은 ', energy_direction, '이고 ', perception, '이며 ', decision, '이며 ', life_style, '입니다.')
        break # 성공적인 분석시 종료
    else: # MBTI 유형을 잘못입력함
        print('MBTI를 잘못 입력했습니다. 다시 입력해주세요.')
