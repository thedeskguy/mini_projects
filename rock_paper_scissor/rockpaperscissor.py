import random as r
paper=r'''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|     
'''
rock=r'''
                _
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
'''
sci=r'''
          _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \
|___/\___|_|___/___/\___/|_|  |___/
'''
option=[rock,paper,sci]
choose=int(input("Choose 0 for rock \n1 for paper \n2 for scissors\n"))
try:
    hum=option[choose]
    print("You Chose")
    print(hum)
    print("Computer chose")
    num=r.randint(0,2)
    comp=option[num]
    print(comp)
    if(comp==hum):
        print("Tie")
    elif((comp==paper and hum==rock) or (comp==rock and hum==sci) or (comp==sci and hum==paper)):
        print("Computer won")
    else:
        print("You won")
except:
    print("Invalid input")