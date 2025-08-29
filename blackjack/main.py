import random
from art import logo 
def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(u_score,comp_score):
    if u_score==comp_score:
        return "Its a draw"
    elif comp_score==0:
        return "You lost the computer has a blackjack"
    elif u_score==0:
        return "Congrats you have a blackjack"
    elif comp_score>21:
        return "Yayayayy you won the comp has more than 21"
    elif u_score>21:
        return "Ohhh you lost you have more than 21"
    elif u_score>comp_score:
        return "You won"
    else:
        return "You lost"
def play_game():
    print(logo)
    user_cards=[]
    computer_cards=[]
    computer_score=-1
    user_score=-1
    is_game_over=False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"Your cards {user_cards} and current score id {user_score}")
        print(f"Computer first card is {computer_cards[0]}")
        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            user_should_deal=input("Type 'y' to deal another card else type 'n' ").lower()
            if user_should_deal=='y':
                user_cards.append(deal_card())
            else:
                is_game_over=True
    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)
        # print(computer_cards)

    print(f"Your final hand is {user_cards} and the score is {user_score}")
    print(f"The computer final hand is {computer_cards} and the final score is {computer_score}")
    print(compare(user_score,computer_score))
    while input("If you wanna continue playing type 'y' else type 'n' ")=='y':
        print("\n"*20)
        play_game()
play_game()
