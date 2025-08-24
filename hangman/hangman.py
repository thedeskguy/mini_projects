import random
import hangman_words as hw
from hangman_art import stages,logo
lives=6
word=random.choice(hw.word_list)
print(logo)

placeholder=""
word_len=len(word)
placeholder="_" * word_len
print(placeholder,"\n")
correct_letter=[]
game_over=False

while not game_over:
    print(f"********{lives}/6 left. Be careful!!*******")
    guess=input("Guess a letter of the word: ").lower()
    print(guess)
    if guess in correct_letter:
        print(f"You already guessed {guess}")
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
    if guess not in word:
        lives-=1
        print(f"You guessed {guess}, thats not in the word. You lose a life")
        if lives==0:
            game_over=True
            print(f"You lost the correct word is {word}")
    if "_" not in display:
        game_over=True
        print("You win")
    print(stages[lives])

