import random
import mysql.connector


# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

winsbot=0
winsuser=0
rock=0
spock=0
paper=0
lizard=0
scissors=0
tempbotwins=0
tempuserwins=0

def name_to_number(name):
    if(name == 'rock'):
        return 0;
    elif(name == 'spock'):
        return 1;
    elif(name == 'paper'):
        return 2;
    elif(name == 'lizard'):
        return 3;
    elif(name == 'scissors'):
        return 4;
    else:
        print( "ERROR Name")
def number_to_name(number):

    if(number == 0):
        return 'rock';
    elif(number == 1):
        return 'spock';
    elif(number == 2):
        return 'paper';
    elif(number == 3):
        return 'lizard';
    elif(number == 4):
        return 'scissors';
    else:
        print ("ERROR Number")
def rpsls(player_choice):
    winsbot=0
    winsplayer=0

    temprock=0
    tempspock=0
    temppaper=0
    templizard=0
    tempscissors=0


    print ("\n")


    print ("Player chooses " + player_choice)

    player_number = name_to_number( player_choice )

    if(player_number == 0):
        temprock+=1
    elif(player_number == 1):
        tempspock+=1
    elif(player_number == 2):
        temppaper+=1
    elif(player_number == 3):
        templizard+=1
    elif(player_number == 4):
        tempscissors+=1

    comp_number = random.randrange( 0, 4 )

    comp_choice = number_to_name( comp_number )

    print ("Computer chooses " + comp_choice)

    difference = (comp_number - player_number) % 5

    if( difference == 1 or difference == 2 ):
        print ("Computer wins!")
        winsbot+=1
    elif ( difference == 4 or difference == 3 ):
        print ("Player wins!")
        winsplayer+=1
    elif( difference == 0 ):
        print ("Player and computer tie!")
    return winsplayer, winsbot, temprock, tempspock, temppaper, templizard, tempscissors
choice="j"

while(choice=="j"):

    print("0 - rock")
    print("1 - Spock")
    print("2 - paper")
    print("3 - lizard")
    print("4 - scissors")
    print("You can choose a number or a word")
    user = input().lower()

    temprock2=0
    tempspock2=0
    temppaper2=0
    templizard2=0
    tempscissors2=0

    if user!="rock" and user!="spock" and user!="paper" and user!="lizard" and user!="scissors":
        user_int = int(user)

        tempbotwins,tempuserwins, temprock2, tempspock2, temppaper2, templizard2, tempscissors2=rpsls(number_to_name(user_int))
    else:
        tempbotwins,tempuserwins, temprock2, tempspock2, temppaper2, templizard2, tempscissors2=rpsls(user)

    winsbot+=tempbotwins
    winsuser+=tempuserwins
    rock+=temprock2
    spock+=tempspock2
    paper+=temppaper2
    lizard+=templizard2
    scissors+=tempscissors2
    print()
    print("Aktuelle Wins:")
    print("Wins User: ", winsuser)
    print("WinsBot: ",winsbot)
    print(rock,spock,paper,lizard,scissors)
    print("\n")
    choice=input("weiterspielen? [j,n]")
print("ENDSTAND")
print("Wins Bot: ",winsbot)
print("Wins User: ",winsuser)

mydb = mysql.connector.connect(
    host="localhost",
    user="java",
    password="java",
    database="python"
)

mycursor = mydb.cursor()

sql = "INSERT INTO ergebnisse VALUES (%s, %s, %s, %s, %s)"
val = (rock,spock,paper,lizard,scissors)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")