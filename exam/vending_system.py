# 자판기 판매 시스템

print('안녕하세요! 자판기 판매 시스템입니다.')
admin_password = '1234' # 관리자 비밀번호
products = ['볼펜', '노트', '가위', '시계'] # 제품
prices = [1000, 1500, 2000, 5000] # 제품의 가격
# 사용자의 모드 (1. 관리자 모드, 2. 고객 모드)
input_mode = int(input('사용할 모드의 번호를 입력해주세요(1. 관리자 모드, 2. 고객 모드): '))

# 관리자 모드
if input_mode == 1:
    # 입력받은 비밀번호
    input_pw = input('관리자 비밀번호를 입력하세요: ')
    if input_pw == admin_password:
        # 사용자가 원하는 옵션 (3. 제품 등록, 4. 제품 삭제)
        input_option = int(input('원하시는 옵션을 입력하세요(3. 제품 등록, 4. 제품 삭제): '))
        if input_option == 3: # 제품 추가
            print('현재 제품 현황: ', products)
            input_product = input('추가할 제품을 입력하세요: ')
            if input_product in products:
                print('입력하신, ', input_product, '는 이미 있습니다.')
            else:
                products.append(input_product)
                prices.append(2500)
                print('입력하신, ', input_product, '(이)가 추가되었습니다.')
                print('현재 제품 현황: ', products)

        elif input_option == 4: # 제품 삭제
            print('현재 제품 현황: ', products)
            input_delete = input('삭제할 제품을 입력하세요: ')
            if input_delete in products:
                for i in range(len(products)):
                    if products[i] == input_delete:
                        products.remove(input_delete)
                        prices.pop(i)
                        break
                print('입력하신, ', input_delete, '(이)가 삭제되었습니다.')
                print('현재 제품 현황: ', products)
            else:
                print('입력하신, ', input_delete, '는 없는 물건입니다.')
        else: # 없는 옵션
            print('입력하신 옵션은 없습니다. 처음부터 진행해주세요.')
    else: # 비번 잘못 입력
        print('비밀번호를 잘못 입력했습니다. 처음부터 진행해주세요.')

# 고객 모드
elif input_mode == 2:
    print('현재 제품 현황: ', products)
    input_product = input('안녕하세요! 구입할 제품 이름을 입력하세요: ')
    if input_product in products:
        input_count = int(input('구입할 제품 개수를 입력하세요: '))
        price = 0
        for i in range(len(products)):
            if products[i] == input_product:
                price = prices[i]
        print('고객님이 구입한 ', input_product, ', ', input_count, '개 ', price * input_count, '원 입니다!')
    else:
        print('입력하신, ', input_product, '는 없는 제품입니다.')

# 없는 모드
else:
    print('입력하신 모드는 없는 모드입니다. 다시 입력해주세요.')
