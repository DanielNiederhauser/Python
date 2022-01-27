class Knoten:
    def __init__(self, daten):
        self.daten = daten
        self.next = None
class VerketteteListe:
    def __init__(self):
        self.kopf = None

    def AmAnfang(self, data_in):
        NeuerKnoten = Knoten(data_in)
        NeuerKnoten.next = self.kopf
        self.kopf = NeuerKnoten


    def KnotenLoeschen(self, LoeschSchluessel):
        Kopfdaten = self.kopf

        if (Kopfdaten is not None):
            if (Kopfdaten.data == LoeschSchluessel):
                self.kopf = Kopfdaten.next
                Kopfdaten = None
                return
        while (Kopfdaten is not None):
            if Kopfdaten.data == LoeschSchluessel:
                break
            prev = Kopfdaten
            Kopfdaten = Kopfdaten.next

        if (Kopfdaten == None):
            return

        prev.next = Kopfdaten.next
        Kopfdaten = None

    def ListeAusgeben(self):
        printval = self.kopf
        while printval.next!=None:
            print(printval.data),
            printval = printval.next

liste = VerketteteListe()
liste.kopf=Knoten(1)
el2=Knoten(2)
el3=Knoten(3)
el4=Knoten(4)

liste.kopf.next=el2
el2.next=el3
el3.next=el4

liste.ListeAusgeben()
