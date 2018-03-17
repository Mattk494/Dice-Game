# This is really damn good
import pickle
import sys
import math
import random

Username=['Ofoog']
Passwords=['go']

f_myfile=open('myfile.pickle', 'ab')
pickle.dump(Username, f_myfile)
f_myfile.close()

f_myfile = open('myfile.pickle', 'rb')
Username = pickle.load(f_myfile)
f_myfile.close()

f_myfiles=open('myfiles.pickle', 'ab')
pickle.dump(Passwords, f_myfiles)
f_myfiles.close()

f_myfiles = open('myfiles.pickle', 'rb')
Passwords = pickle.load(f_myfiles)
f_myfiles.close()

print(Username)
print(Passwords)

EnterUsername=input("Enter Your Username")
Password= input ("Enter Your Password")

while EnterUsername not in Username:
    print("You need to create an account")
    EnterUsername=input("Enter A Username")
    Password= input ("Enter A Password")

    Username.append(EnterUsername)
    f_myfile=open('myfile.pickle', 'wb')
    pickle.dump(Username, f_myfile)
    f_myfile.close()

    f_myfile = open('myfile.pickle', 'rb')
    Username = pickle.load(f_myfile)
    f_myfile.close()

    print(Username)

    Passwords.append(Password)

    f_myfiles=open('myfiles.pickle', 'wb')
    pickle.dump(Passwords, f_myfiles)
    f_myfiles.close()

    f_myfiles = open('myfiles.pickle', 'rb')
    Passwords = pickle.load(f_myfiles)
    f_myfiles.close()

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
                    print ("You Rolled a", Dicerolls)
                    while Counter> 0:
                        Y= random.randint(1,6)
                        X= X+Y
                        Counter=Counter-1
                else:
                    sys.exit()

if X>Rollneed:
    print("You win" , "Your Score was", X)
