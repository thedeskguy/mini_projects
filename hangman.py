import random
# print("""
#  _                                             
# | |                                            
# | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
# | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
# | | | | (_| | | | | (_| | | | | | | (_| | | | |
# |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
#                     __/ |                      
#                    |___/                       

# """)

stages=[
    '''
        _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
     |___''',
     '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
     |___''',
        '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       
     |       
     |
     |___''',
         '''
      _______
     |/      |
     |      (_)
     |      \|
     |       
     |       
     |
     |___''',
         '''
      _______
     |/      |
     |      (_)
     |      
     |       
     |       
     |
     |___''',
         '''
      _______
     |/      |
     |      
     |      
     |       
     |       
     |
     |___'''
]
word_list=["batman","spiderman","superman","camel"]

word=random.choice(word_list)
print(word)

placeholder=""
word_len=len(word)
placeholder="_" * word_len
print(placeholder)
correct_letter=[]
game_over=False

while not game_over:
    guess=input("Guess a letter of the word: ").lower()
    print(guess)

    display=""
    for char in word:
        if char==guess:
            display+=char
            correct_letter.append(char)
        elif char in correct_letter:
            display+=char
        else:
            display+="_"
    print(display)
    if "_" not in display:
        game_over=True
        print("You win")

