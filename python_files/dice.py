
Username=['Ofoog']
Passwords=['go']

import pickle

with open ('users.pkl','rb') as L:
    Username= pickle.load(L)

with open('passs.pkl','rb') as T:
    Passwords= pickle.load(T)

EnterUsername=input("Enter Your Username")
Password= input ("Enter Your Password")

while EnterUsername not in Username:
    print("You need to create an account")
    EnterUsername=input("Enter A Username")
    Password= input ("Enter A Password")
    Username.append(EnterUsername)
    with open('userss.pkl','wb') as L:
        pickle.dump(Username, L)
    Passwords.append(Password)
    with open('passs.pkl','wb') as T:
        pickle.dump(Passwords, T)
print(Username)
print (Passwords)

while EnterUsername in Username:
    X= Username.index(EnterUsername)
    while Password != (Passwords[X]):
        print ("Wrong Password. Try Again")
        Password= input ("Enter Your Password")

    if Password == (Passwords[X]):

        Dicerolls=int(input("Select how many dice you want to roll."))
        Counter= 0 + Dicerolls
        Rollneed=Dicerolls*5
        X=0
        import math
        import random
        print ("You have to roll a total score of", Counter*5 , "to win")


        while Counter> 0:
            Y= random.randint(1,6)
            X= X+Y
            Counter=Counter-1

            if X <Rollneed:
                print("You lose", "Your Score was only", X)
                Playagain= str (input("Would you like to play again. Y/N"))
                if Playagain == "Y":
                    Dicerolls=int(input("Select how many dice you want to roll"))
                    Counter= 0 + Dicerolls
                    Rollneed=Dicerolls*5
                    X=0
                    print ("You have to roll a total score of", Counter*5 , "to win")
                    while Counter> 0:
                        Y= random.randint(1,6)
                        X= X+Y
                        Counter=Counter-1
                else:
                    import sys
                    sys.exit()

if X>Rollneed:
    print("You win" , "Your Score was", X)
