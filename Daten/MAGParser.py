import Datenbank.DQL as dql
import Datenbank.Einfügen as inst
import Daten.MAG as mag
import json

punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~üöä1234567890'''



def parseZitate():
    titelliste = dql.hundertpublikation()
    for row in titelliste:
        orginaltitel = row[0]
        titel = row[0]
        #Titel anpassen
        #alle Sonderzeichen werden raus gefiltert
        for ele in titel:
             if ele in punc:
                 titel = titel.replace(ele, "")
        titel = titel.lower()
        titel = titel.strip()

        js = mag.sucheZitate(titel)
        if js == None:
            break
        else:
            datenausjsonextrahieren(js, orginaltitel)


# Hier wird aus beiden suchen die json extrahiert und zerlegt
# Keine Rückgabe
def datenausjsonextrahieren(js, orginaltitel):
    #Alle enteties in der Antwort werden durchsucht
    for entity in js["entities"]:
        try:
            #versucht Citcon zufinden, falls nicht gibt es keine Zitate in dieser entity
            for zitattitelid in entity["CitCon"]:
                titelenitity = mag.sucheTitel(zitattitelid)
                for titelentities in titelenitity["entities"]:
                    suchePublikationen(entity, orginaltitel, titelentities, zitattitelid)
        except:
            print("Kein Zitat gefunden")



# Hier wird für die einzelnen Titel die passende Id für die hat_zitat Relation rausgesucht
# Keine Rückgabe
def suchePublikationen(entity, orginaltitel, titelentities, zitattitelid):
    try:
        #Wert der Id ist das Zitat
        zitat = entity["CitCon"][zitattitelid]
        hatzitatid = dql.suchePublikationsId(orginaltitel)
        istzitatid = dql.suchePublikationsId(titelentities["DN"])
        if istzitatid != None:
            inst.insertPublikation_hat_Zitat(hatzitatid, istzitatid, zitat[0])

    except Exception as e:
        print(e)
        print("Kein Titel gefunden")


parseZitate()