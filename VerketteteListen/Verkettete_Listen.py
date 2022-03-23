import random, time
class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None


class LListe:
    def __init__(self, firstNode=None):
        self.length=0
        self.head = firstNode
        self.tail=None

    def append(self, NewNode):
        NewNode.next = None
        if self.head == None:
            NewNode.previous = None
            self.head = NewNode
            return
        last = self.head
        while (last.next != None):
            last = last.next
        last.next = NewNode
        NewNode.previous = last

    def insertAfter(self, prevNode, newNode):
        if prevNode == None:
            print("Node nicht vorhanden! ")
        else:
            newNode.next=prevNode.next
            prevNode.next = newNode
            newNode.previous=prevNode
            if newNode.next != None:
                newNode.next.previous=newNode

    def insertBefore(self,nextNode, newNode):
        if nextNode == None:
            print("Node nicht vorhanden")
        else:
            if nextNode == self.head:
                temp = self.head
                self.head = newNode
                newNode.next = temp
                temp.previous = newNode
                newNode.previous = None
                return
            newNode.previous = nextNode.previous
            nextNode.previous = newNode
            newNode.next = nextNode
            if newNode.previous:
                newNode.previous.next = newNode



    def deleteAfter(self, ausgangsNode):

        if ausgangsNode.next==None:
            print("Letztes Element der LListe")
            return
        if ausgangsNode.next.next==None:
            ausgangsNode.next= None
            return
        else:
            ausgangsNode.next.next.previous=ausgangsNode
            ausgangsNode.next=ausgangsNode.next.next



    def deleteBefore(self, ausgangsNode):
        if ausgangsNode==None or self.head==ausgangsNode:
            print("Falsche Eingabe: Eingabe entweder null oder erstes Element")
            return
        if ausgangsNode.previous.previous == None:
            #Erstes Element wird gelöscht
            ausgangsNode.next.previous = None
            self.head=ausgangsNode
        else:
            ausgangsNode.previous.previous.next=ausgangsNode
            ausgangsNode.previous=ausgangsNode.previous.previous


    def findByIndex(self,index):
        if self.head==None:
            print("Liste leer")
            return
        aktuelles = self.head
        count = 1
        while True:
            if aktuelles==None:
                print("Nicht vorhanden!")
                return False
            if count==index:
                print(aktuelles.value)
                return
            count+=1
            aktuelles=aktuelles.next
    def sortASC(self):
        """if self.head!= None:
            temp = self.head
            while temp.next!=None:
                index = temp.next
                while index!= None:
                    if temp.value >index.value:
                        temp1 = temp.value
                        temp.value = index.value
                        index.value = temp1
                    index = index.next
                temp = temp.next"""

        """key = self.head
        while key != None:
            start = self.head
            while key !=start:
                if key.value<start.value:
                    self.insertAfter(start.previous, Node(key.value))
                    self.deleteAfter(key.previous)
                    break
                start = start.next
            key = key.next"""
        if self.head==None:
            return
        else:
            current = self.head
            while current.next!=None:
                index = current.next
                while index!=None:
                    if current.value>index.value:
                        temp = current.value
                        current.value=index.value
                        index.value=temp
                    index=index.next
                current=current.next
    def sortDESC(self):
        if self.head!= None:
            temp = self.head
            while temp.next!=None:
                index = temp.next
                while index!= None:
                    if temp.value <index.value:
                        temp1 = temp.value
                        temp.value = index.value
                        index.value = temp1
                    index = index.next
                temp = temp.next
    def printAll(self, list=None):
        ausgabelist=[]
        temp = self.head
        while temp != None:
            ausgabelist.append(temp.value)
            temp=temp.next
        print(ausgabelist)

class ArrayListe:
    def __init__(self, vorgegebeneList = []):
        self.list = vorgegebeneList

    def append(self,value):
        self.list.append(value)

    def insertAfter(self,index,value):
        #Bei index=0 wird die value zwischen 0 und 1 geschrieben
        # (erstes Element = Stelle0)
        if index>len(self.list):
            print("Index höher als Listengroeße")
            return False
        self.list.insert(index+1,value)

    def insertBefore(self,index,value):
        #Bei index=1 wird die value zwischen Element 0 und 1 geschrieben
        #index=0 --> Value wird an die allererste Stelle der Liste eingefügt

        if index>len(self.list):
            print("Index höher als Listengroeße")
            return False
        self.list.insert(index,value)
    def deleteAfter(self,index):
        #Bei index=0 wird das zweite Element der Liste gelöscht
        # (Annahme: Erstes Element ist Index 0)
        if index>len(self.list):
            print("Index höher als Listengroeße")
            return False
        self.list.remove(index+2)
    def deleteBefore(self,index):
        #Bei index=1 wird das 0te Element gelöscht
        #index=0 ergibt keinen Sinn
        if index==0:
            print("Das Element vor dem ersten Element (an Stelle 0) zu löschen,"
                  "ergibt keinen Sinn")
            return False
        if index>len(self.list):
            print("Index höher als Listengroeße")
            return False
        self.list.remove(index)
    def findByIndex(self,index):
        #index=0 returnt die Value an der 0ten Stelle
        if index+1>len(self.list):
            print("Index höher als Listengroeße")
            return False
        return self.list[index]
    def sortASC(self):
        for i in range(1, len(self.list)):
            key = self.list[i]

            j = i-1
            while j >= 0 and key < self.list[j] :
                self.list[j + 1] = self.list[j]
                j -= 1
            self.list[j + 1] = key
    def sortDESC(self):
        for i in range(1, len(self.list)):
            key = self.list[i]

            j = i-1
            while j >= 0 and key > self.list[j] :
                self.list[j + 1] = self.list[j]
                j -= 1
            self.list[j + 1] = key
    def printArrayList(self):
        print(self.list)

if False: #Testzwecke
    element1 = Node(1)
    element2 = Node(2)
    element3 = Node(3)
    element4 = Node(4)
    element5 = Node(5)
    list = LListe(element1)
    list.append(element2)
    list.append(element3)
    list.append(element4)
    #list.insertAfter(element4,element5)
    list.insertBefore(element2,element5)
    #list.deleteAfter(element3)
    #list.deleteBefore(element4)
    list.findByIndex(6)
    list.sortDESC()

    print("Alle Elemente ausgeben")
    list.printAll()
    #list.printfirst()
if False: #Testzwecke
    aList = ArrayListe([17,123,3213,1,2,3,5,7,1,2,-1,-2])
    #aList.insertAfter(0,9)
    #aList.insertBefore(0,3)
    #aList.deleteAfter(0)
    #aList.deleteBefore(1)
    #print(aList.findByIndex(7))
    #aList.sortASC()
    #aList.sortDESC()
    aList.printArrayList()

def randomZahlen(anzahl, min, max):
    c = []
    for i in range((anzahl)):

        c.append(random.randint(min,max))
    return c
def printZahlen(arr):
    for i in range(len(arr)):
        print(arr[i])
if __name__ =="__main__":
    llist = LListe();
    anzahl = 10000
    min = 0
    max = 10000
    zufallszahlen = randomZahlen(anzahl,min,max)
    #printZahlen(zufallszahlen)
    aL = ArrayListe()

    startEinfuegenArrayList = time.time()
    for i in range(anzahl):
        aL.append(zufallszahlen[i])
    endeEinfuegenArrayList = time.time()
    einfuegZeitArrayList = endeEinfuegenArrayList-startEinfuegenArrayList
    #Einheit: Sekunden --> *1000 um Millisekunden zu bekommen
    print("Einfügzeit Arraylist: ",'{:5.10f}'.format(einfuegZeitArrayList*1000), "Millisekunden")
    #print("Type: ", type(aL))
    #aL.printArrayList()

    startEinfuegenLinkedList = time.time()
    for i in range(anzahl):
        llist.append(Node(zufallszahlen[i]))
    endeEinfuegenLinkedList = time.time()
    einfuegZeitLinkedList = endeEinfuegenLinkedList-startEinfuegenLinkedList
    print("Einfügzeit LinkedList: ",'{:5.10f}'.format(einfuegZeitLinkedList*1000), "Millisekunden")

    print("Type: ",type(llist))
    llist.printAll()
    startSortArrayList = time.time()
    aL.sortASC()
    endeSortArrayList = time.time()
    sortZeitArrayList = endeSortArrayList-startSortArrayList
    aL.printArrayList()

    if sortZeitArrayList>=1:
        print("Sortierzeit ArrayList: ",'{:5.10f}'.format(sortZeitArrayList), "Sekunden")
    else:
        print("Sortierzeit ArrayList: ",'{:5.10f}'.format(sortZeitArrayList*1000), "Millisekunden")

    startSortLinkedList = time.time()
    llist.sortASC()
    endeSortLinkedList = time.time()
    sortZeitLinkedList = endeSortLinkedList-startSortLinkedList
    llist.printAll()
    if sortZeitLinkedList>=1:
        print("Sortierzeit LinkedList: ",'{:5.10f}'.format(sortZeitLinkedList), "Sekunden")
    else:
        print("Sortierzeit LinkedList: ",'{:5.10f}'.format(sortZeitLinkedList*1000), "Millisekunden")
