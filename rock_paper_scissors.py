import random
import time

user_win = 0
pc_win = 0
result = 0

while True:
    if(result >= 1):
        print(f"User wins : {user_win}\nComputer wins : {pc_win}")

    user_input = input("Please enter Rock/Paper/Scissors or Q to quit : ").lower()
    if(user_input == "q"):
        print("Sad to see you go without playing :(")
        time.sleep(1)
        quit()
    elif( user_input not in ["rock","paper","scissors"]):
        continue
    elif( user_input in ["rock","paper","scissors"]):
        pc_choise = random.randint(0,2)
        if(pc_choise == 0):
            pc_rps = "rock"
        elif(pc_choise == 1):
            pc_rps = "paper"
        else:
            pc_rps = "scissors"
        if(pc_rps == user_input):
            print("DRAW!")
        elif(pc_rps == "rock"):
            if(user_input == "paper"):
                print("You win")
                user_win+=1
            elif(user_input=="scissors"):
                print("Computer wins")
                pc_win+=1
        elif(pc_rps=="paper"):
            if(user_input=="rock"):
                print("Computer wins")
                pc_win+=1
            elif(user_input=="scissors"):
                print("You win")
                user_win+=1
        elif(pc_rps=="scissors"):
            if(user_input=="rock"):
                print("You win")
                user_win+=1
            elif(user_input == "paper"):
                print("Computer wins")
                pc_win+=1
    result+=1


        