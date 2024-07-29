import random
secretNumber = random.randint(1,20)
print("I'm thinking of a number between 1 to 20")

for i in range(1,7):
    print('Take a guess')
    guess = int(input())
    if guess<secretNumber:
        print('Guess is too low')
    elif guess>secretNumber:
        print('Guess is too high')
    else:
        break

if guess == secretNumber:
    print('Excellent' + str(i) + 'guesses!')
else:
    print('Nope ! Wrong Guess' + str(secretNumber))

