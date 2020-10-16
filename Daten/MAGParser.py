import Datenbank.DQL as dql
import Daten.MAG as mag
import json

punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~üöä1234567890'''



def parseZitate():
    titelliste = dql.hundertpublikation()
    orginaltitel = ""
    for row in titelliste:
        orginaltitel = row[0]
        titel = row[0]
        for ele in titel:
             if ele in punc:
                 titel = titel.replace(ele, "")
        titel = titel.lower()
        titel = titel.strip()
        print(titel)
        js = mag.sucheZitate(titel)
        if js == None:
            break
        else:
            print(json.dumps(js, indent=3))
            for entities in js["entities"]:
                try:
                    # print(json.dumps(entities["CitCon"], indent=3))
                    for zitat in entities["CitCon"]:
                        titelenitity = mag.sucheTitel(zitat)
                        for titelentities in titelenitity["entities"]:
                            try:
                                # print(json.dumps(entities["CitCon"], indent=3))
                                # print(zitat)
                                print(titelentities["DN"])
                                print(orginaltitel)
                                # print(entities["CitCon"][zitat])
                                hatzitatid = dql.suchePublikationsId(orginaltitel)
                                istzitatid = dql.suchePublikationsId(titelentities["DN"] + ".")
                                print(hatzitatid)
                                print(istzitatid)




                            except:
                                print("Kein Titel gefunden")
                except:
                    print("Kein Zitat gefunden")


parseZitate()