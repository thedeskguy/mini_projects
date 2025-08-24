from art import logo
print(logo)
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]


def caeser(text,shift,cipher):
    output=""
    if cipher=="decode":
        shift*=-1
    for char in text:
        if char not in alphabets:
            output+=char
        else:
            ind=(alphabets.index(char)+shift)%26
            output+=alphabets[ind]
    print(f"Your {cipher}d message is {output}")
    
should_continue=True
while should_continue:
    direction=input(r"Type 'encode' to encrypt, or 'decode' to decrypt \n ").lower()
    text=input("Type your message \n").lower()
    shift=int(input("Type your shift number \n"))    
    caeser(text,shift,direction)
    restart=input("If you wanna continue type 'yes' else 'no'\n").lower()
    if restart=="no":
        should_continue=False
        print("Goodbye")