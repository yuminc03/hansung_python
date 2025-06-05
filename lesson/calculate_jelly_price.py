# jellyPrice = 700
# jellyCount = int(input('구입 수량을 입력하세요 (젤리 1개 = 700원) : '))
# print('젤리', jellyCount, '개의 가격:', jellyCount * 700)

# a = 700
# b = int(input('수량 : '))
# print('총금액 : ' + (a*b))

jellyPrice = 700
jellyCount = int(input('구입 수량을 입력하세요: '))
money = int(input('젤리를 살 금액을 입력하세요: '))
total = jellyPrice * jellyCount
print('=============================')
print('총 젤리 가격:', jellyCount * jellyPrice)
print('----------------------------------------')
print('거스름돈: ', (money - total))

remaining = money - total
print('1000원: ', remaining // 1000, '장')

h = (remaining % 1000) // 100
print('100원: ', h, '개')
