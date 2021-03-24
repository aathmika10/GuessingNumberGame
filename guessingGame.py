import random
number= random.randint(1,10)
chances=0

while chances   < 5:
    guess= int(input("Enter your guess between numbers 1-9: "))
    
    if guess==number:
        print("Congradulations YOU WON  !!!")
        break
    elif guess>number:
        print("Higher than the number")
    elif guess<number:
         print("Lower than the number")
    if not chances<5    :
        print("YOU LOSE!!! The number is ", number)