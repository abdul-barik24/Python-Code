# random guess game
from random import randint
# generate a number 1~10
answer = randint(1, 10)

while True:
    try:
        # input from user?
        guess = int(input(('Guess a number 1~10: ')))
        # check that input is number 1~10
        if 0 < guess < 11:
            if guess == answer:
                print('Your are a genius!')
                break
            else:
                print('The currect answer is: ' , answer)
        else:
            print('Hey, I said 1~10.')
    except ValueError:
        print('Please, enter a number.')
        continue

# check if number is rigth guess
# otherwise ask again




