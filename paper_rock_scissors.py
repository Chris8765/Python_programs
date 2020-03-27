#gra: Kamień, papier nożyczki.

import random
response = None
w1 = None
w2 = None
p1 = None
p2 = None

def instruction():
    
    print("Instruciton:\n")
    print("en.wikipedia.org/wiki/Rock_paper_scissors")

    

def human_move():
    human_choice = None
    
    while human_choice not in ("p", "r", "s"):
        human_choice = str(input("What do you choose? paper (write: p), rock (write: r) or scissors(write: s)? "))
    
    if human_choice =="p":
        w1 = "paper"
        print ("You chose: paper")
    elif human_choice == "r":
        w1 = "rock"
        print ("You chose: rock")
    elif human_choice == "s":
        w1 = "scissors"
        print ("You chose: scissors")
    
    return w1

def computer_move():
    
   
    computer_choice = random.randint(1,3)
    
    if computer_choice == 1:
        w2 = ("paper")
    elif computer_choice == 2:
        w2 = ("rock")
    elif computer_choice == 3:
        w2 = ("scissors")
    print("Computer choses: ", w2)
    return w2


    
    
def rps(p1, p2):

    
    
    if p1 == ("scissors") and p2 == ("paper"):
        response = ("Human won!")
        return response
    elif p1 == ("scissors") and p2 == ("rock"):
        response = ("Computer won!")
        return response
    elif p1 == ("paper") and p2 == ("scissors"):
        response = ("Computer won!")
        return response
    elif p1 == ("paper") and p2 == ("rock"):
        response = ("Human won!")
        return response
    elif p1 == ("rock") and p2 == ("paper"):
        response = ("Computer won!")
        return response
    elif p1 == ("rock") and p2 == ("scissors"):
        response = ("Human won!")
        return response
    elif p1 == ("rock") and p2 == ("rock"):
        response = ("Draw!")
        return response
    elif p1 == ("paper") and p2 == ("paper"):
        response = ("Draw!")
        return response
    elif p1 == ("scissors") and p2 == ("scissors"):
        response = ("Draw!")
        return response
    
    
def winner(response):
    print(response)
    
def main():
    instruction()
    p1 = human_move()
    p2 = computer_move()
    response = rps(p1, p2)
    winner(response)
        
main()

input("\n\n If you want to finish press enter..")
 