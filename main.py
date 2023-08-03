import random


print("---------Let's start our game-----------\n \n ")

def computer_choice():
    choices =["snake", "water", "gun"]
    return random.choice(choices)
    

won=0
lost = 0

def ifwin():
    global won
    won = won +1

def iflost():
    global lost
    lost = lost +1


def start():
    comp =computer_choice()
    player_input=input("Please choose your option 'snake or  water or gun' : ")

    print(f"\n player's option: {player_input}")
    print(f"Computer's option: {comp} \n")

    if player_input =="snake": # first condition
        if comp =="snake":
            print("Game Drawn, both player choose same option")
        elif comp=="water":
            print("player won the match \n Snake drank the water") 
            ifwin() 
        elif comp =="gun":
            print("player lost the match \n Snake killed by Gun")
            iflost()
    elif player_input =="water": # second condition
        if comp =="snake":
            print("player lost the match \n Snake drank the water")
            iflost()
        elif comp=="water":
            print("Game Drawn, both player choose same option")   
        elif comp =="gun":
            print("player Won the match \n Water ne gun kharaab kr di")
            ifwin()
    elif player_input =="gun": # third condition
        if comp =="snake":
            print("player Won the match \n Snake killed by Gun")
            ifwin()
        elif comp=="water":
            print("player lost the match \n Water ne gun kharaab kr di") 
            iflost()  
        elif comp =="gun":
            print("Game Drawn, both player choose same option")
    else:
        print("please enter correct option \n")
    print(f" \n Total times when Player won: {won} \n")
    print(f"Total times when Computer won: {lost} \n")
    


output="y"
while output=="y":
    if output=="y":
        start()
        print("\n Next Round \n \n ")
        output = input(" \n do you want to play the game again ' y/n ' :  \n")

    elif output =="n": 
        print(" \n Thank you for playing the game \n \n ")
        break
        

