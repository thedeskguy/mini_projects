import random
word_list=["batman","spiderman","superman","camel"]

word=random.choice(word_list)
print(word)

guess=input("Guess a letter of the word: ").lower()
print(guess)

for char in word:
    if char==guess:
        print("right")
    else:
        print("wrong")
