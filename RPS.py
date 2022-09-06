import random

    print("choose a number between 1-3")
    user=input("rock=1,paper=2 and Scissors=3 \n")
    computer = random.randint(1,3)
    user=int(user)
    print(computer )
    print(user)
    if(user==1 and computer==3):
      print("user won")
    elif(user==1 and computer==2):
      print("computer won")
    elif(user==1 and computer==1):
      print("draw")
    elif(user==2 and computer==1):
      print("user won")
    elif(user==2 and computer==3):
      print("computer won")
    elif(user==2 and computer==2):
      print("draw")
    elif(user==3 and computer==2):
      print("user won")
    elif(user==3 and computer==1):
      print("computer won")
    elif(user==3 and computer==3):
      print("draw")