import random
r = random.randint(1, 100)
while True:
    num = input('guess a number: ')
    num = int(num)
    if num == r:
        print('你猜對了!')
        break
    elif num > r:
        print('數字猜太大囉')
    elif num < r:
        print('數字猜太小囉')

    




