import random

def usereingabe():
    eingabe=''
    while(eingabe!='s' and eingabe!='t' and eingabe!='p'):
        eingabe = input("Schere(s), Stein(t) oder Papier(p)? ")
    return eingabe

moeglichkeiten = ["s", "t", "p"]
choice='j'
while choice =='j':
    user = usereingabe()

    temp = random.randint(0,2)
    bot = moeglichkeiten[temp]
    print("Bot: "+bot)
    print("User: "+user)

    if bot == user:
        print("unentschieden")
        exit()
    elif (bot=='s' and user=='p') or (bot=='p' and user=='t') or (bot=='t' and user=='s'):
        print("Bot gewinnt")
    else:
        print("User gewinnt")
    print("\n")
    choice = input("Weiterspielen? j.. ja ")
