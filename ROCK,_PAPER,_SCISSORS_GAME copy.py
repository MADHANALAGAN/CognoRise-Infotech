import random

def game(computer,user):
    if (computer=="rock" and user =="paper") or (computer=="paper" and user =="scissors") or (computer=="scissors" and user =="rock") :
        return "win"
    elif (computer=="rock" and user =="scissors") or (computer=="paper" and user =="rock") or (computer=="scissors" and user =="paper"):
        return "lose"   
    else:
        return "tie"
    

user_score=0            
while True:

        print("")
        # get user choice
        user=input("rock,paper,scissors :").lower()
        if user not in ["rock","paper","scissors"]:
            print("Invalid input! Please enter either 'rock', 'paper', or 'scissors'")
            continue
        else:
            #get_computer_choice
            computer=random.choice(["rock","paper","scissors"])
            print("")
            print("your choice is :",user)
            print("computer choice is :",computer)
            print("")

            result=game(computer,user)
            if result in ("win","lose"):
                 print("! you ",result,"!")
            else:
                print("It's a tie!")


        if result == "win":
            user_score += 10
        elif result == "lose":
            user_score -= 10
        print(f"Scores - You: {user_score}")
            

        play_again=input("\ndo you play again say(yes/no)").lower()
        if play_again != "yes":
            print("GAME OVER")
            break
    
  

