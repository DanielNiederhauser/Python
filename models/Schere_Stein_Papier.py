import random
import mysql.connector
import requests


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

#DB Stuff

def DatabaseErstellen(host, user, pw, name="SWP_Python"):
    db = mysql.connector.connect(host=host, user=user, password=pw)
    cursor = db.cursor()
    cursor.execute("Create database if not exists "+name)

def CreateTable(host, user, pw, dbname="SWP_Python",name="SchereSteinPapier"):
    db = mysql.connector.connect(host=host, user=user, password=pw, database=dbname)
    cursor = db.cursor()
    cursor.execute("Create Table if not exists "+name+
                   " (rock INT, spock INT, paper INT, lizard INT, scissors INT)")

def Insert(rock, spock, paper, lizard, scissors, host, user, pw, dbname="SWP_Python", name="SchereSteinPapier"):
    db = mysql.connector.connect(host=host, user=user, password=pw, database=dbname)
    cursor = db.cursor()
    sql = "INSERT INTO "+name+" VALUES ("+rock.__str__()+","+spock.__str__() +","+paper.__str__()+ ","+lizard.__str__()+","+scissors.__str__()+")"
    #print(sql)
    cursor.execute(sql)
    db.commit()
def alleSummen(host, user, pw, dbname="SWP_Python",tablename="SchereSteinPapier"):
    db = mysql.connector.connect(host=host, user=user, password=pw, database=dbname)
    cursor = db.cursor()
    cursor.execute("select sum(rock),sum(spock),sum(paper),sum(lizard),sum(scissors) from "+tablename)
    return cursor.fetchall()[0]
    #Aufruf dieser Methode am besten mit 5 Variablen in der Reihenfolge: (in die 5 Variablen speichern)
    #rock,spock,paper,lizard,scissors

def sendRequest(username, voteScissors, voteRock, votePaper, voteSpock, voteLizard, apiIP = "http://127.0.0.1:5000"):
    reqUrl = apiIP + "/v1/updateRecord"
    reqUrl+= "?username=" + str(username) + "&voteScissors=" + str(voteScissors)
    reqUrl+= "&voteRock=" + str(voteRock) + "&votePaper=" + str(votePaper)
    reqUrl+= "&voteSpock=" + str(voteSpock) + "&voteLizard=" + str(voteLizard)
    responseCode = 0
    try:
        response = requests.post(reqUrl, None)
        responseCode = response.status_code
    except:
        return 0
    return responseCode

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
host="localhost"
user="java"
pw="java"
DatabaseErstellen(host,user,pw)
CreateTable(host,user,pw)

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
    print("Userchoices: ")
    print("Rock: "+rock.__str__()+" Spock:"+spock.__str__()+" Paper: "+paper.__str__()+" Lizard: "+lizard.__str__()+" Scissors: "+scissors.__str__())

    print("\n")
    choice=input("weiterspielen? [j,n]")
print("ENDSTAND")
print("Wins Bot: ",winsbot)
print("Wins User: ",winsuser)

Insert(rock,spock,paper,lizard,scissors,"localhost","java","java")
print("In DB gespeichert")

r,sp,p,l,s =alleSummen("localhost","java","java")
print(r,sp,p,l,s)
code = sendRequest("Niederhauser",scissors,rock,paper,spock,lizard)

print("code="+str(code))