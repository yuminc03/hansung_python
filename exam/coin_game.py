import random

# 동전 게임

count = 0
bingo_count = 0 # 빙고가 나온 횟수

while (True):
    count = count + 1
    print('***', count, '회 동전게임 ***')
    r = random.randrange(0, 2) # 컴퓨터가 random 생성 (앞:0, 뒤:1)
    direction = int(input('앞(0)/뒤(1) 입력: '))

    if r == direction:
        print('Bingo!')
        bingo_count = bingo_count + 1
    else:
        print('Not Bingo...')

    if bingo_count == 3:
        print('빙고를 3번 맞춰서 게임을 종료합니다.')
        print('*** 총 시도 횟수: ', count, '회 ***')
        break