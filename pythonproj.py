import random

comp_point=0
user_point=0
draw=0

print("WELCOME TO THE GAME!!")
print(end="\n")


while True:
    options=["rock","paper","scissor"]
    comp=random.choice(options)
    user=input("Enter r->rock p->paper s->scissor: ")
    print(end="\n")
    
    
    if user=="r":
        user="rock"
    elif user=="p":
        user="paper"
    elif user=="s":
        user="scissor"
        
    if comp==user:
        print("DRAW!! both chose:",comp)
        print(end="\n")
        draw+=1
    elif user=="rock":
        if comp=="paper":
            print("COMPUTER WON!! as it chose:",comp)
            print(end="\n")
            comp_point+=10
        if comp=="scissor":
            print("YOU WON!! as computer chose",comp)
            print(end="\n")
            user_point+=10
    elif user=="paper":
        if comp=="rock":
            print("YOU WON!! as computer chose",comp)
            print(end="\n")
            user_point+=10
        elif comp=="scissor":
            print("COMPUTER WON!! as it chose:",comp)
            print(end="\n")
            comp_point+=10
    elif user=="scissor":
        if comp=="rock":
            print("COMPUTER WON!! as it chose:",comp)
            print(end="\n")
            comp_point+=10
        elif comp=="paper":
            print("YOU WON!! as comp chose",comp)
            print(end="\n")
            user_point+=10
            
    
    
    play=input("To Continue Press y / To End Press n: ")
    print(end="\n")
    if play.lower() !="y":
        print("Computer Point: ",comp_point)
        print(end="\n")
        print("Your Point: ",user_point)
        print(end="\n")
        print("Total Draws: ",draw)
        print(end="\n")
        break
            
            