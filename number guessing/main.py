import random
from art import logo
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5
print(logo)

def check_answer(answer,guess):
    if guess == answer:
        return f"You guessed it right which was {answer}"
    elif guess>answer:
        return "You guessed to high"
    else:
        return "You guessed too low"
def set_difficulty():
    level=input("Choose a difficulty type 'easy' or 'hard' ").lower()
    if level=="easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
def game():    
    print("Welcome")
    print("I am guessing a number between 1 and 100 ")
    answer=random.randint(1,100)
    # print(answer)
    turns=set_difficulty()
    print(f"you have {turns} turns left")
    guess=0
    while turns>0 and guess!=answer:
        guess=int(input("Guess a number "))
        print(check_answer(answer,guess))
        turns-=1
        print(f"you have {turns} turns left")
        if turns==0:
            print("all attempts finished you lose")

game()