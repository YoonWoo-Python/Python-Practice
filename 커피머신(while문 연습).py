coffee = 10
while True:
    if coffee == 0:
        print('===커피가 없습니다===')
        break
    print('                      ')
    print('===커피머신===')
    print('===커피 한잔에 500원===')
    print('                      ')
    money = int(input('돈 넣기 - '))
    if money == 500:
        coffee -= 1
        print('커피 나왔습니다. 남은 커피: %d' %coffee)
    elif money > 500:
        coffee -= 1
        print('커피 나왔습니다. 잔돈은 {0} 남은 커피: {1}'.format(money-500,coffee))
    else:
        print('돈이 %d 원 부족합니다' %(500-money))