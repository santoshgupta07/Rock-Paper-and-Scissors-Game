import random
computer=random.choice([1,0,-1])
youstr=input("Enter your choice (r for rock, p for paper, s for scissors): ")
youDict= {"r":1,"p":0,"s":-1}
reverseDict= {1:"rock",0:"paper",-1:"sciorss"}
you = youDict[youstr]

print(f"Your choice is :{reverseDict[you]}\nComputer choice is :{reverseDict[computer]}")
if(computer==you):
    print("Its draw")
else:
    if(computer==1 and you==0):
        print("you Win!")
    elif(computer==1 and you==-1):
        print("You Loose!")
    elif(computer==0 and you==1):
        print("You Loose!")
    elif(computer==0 and you==-1):
        print("You Win!")
    elif(computer==-1 and you==1):
        print("You Win!")
    elif(computer==-1 and you==0):
        print("You Loose!")
    else:
        print("something went wrong!!!")

