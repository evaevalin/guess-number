import random
r = random.randint(1, 100)
count = 0
while True:
    count += 1 #count = count+1
    num = input('guess a number: ')
    num = int(num)
    if num == r:
        print('你猜對了!')
        print('這是你猜的第',count, '次')
        break
    elif num > r:
        print('數字猜太大囉')
    elif num < r:
        print('數字猜太小囉')
    print('這是你猜的第',count, '次')

    




