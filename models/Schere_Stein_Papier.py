moeglichkeiten = ["s", "t", "p"]
#Schere...0
#Stein...1
#Papier...2
eingabe = input("Schere(s), Stein(t) oder Papier(s)? ")

import random
a = random.randint(0,2)
print(moeglichkeiten[a])


if(eingabe=='s' and a==1):
    print("Du hast verloren")
    #Spieler Schere, Bot Stein
elif(eingabe=='s' and a==2):
    print("Du hast gewonnen")
    #Spieler Schere, Bot Papier

elif(eingabe=='p' and a==2):
    print("Unentschieden")
    #Spieler Papier, Bot Papier