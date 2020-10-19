import Datenbank.DQL as dql
import Datenbank.Einfügen as inst
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
                    for zitattitelid in entities["CitCon"]:
                        titelenitity = mag.sucheTitel(zitattitelid)
                        for titelentities in titelenitity["entities"]:
                            try:
                                # print(json.dumps(entities["CitCon"], indent=3))
                                #print(zitat)
                                print(titelentities["DN"])
                                print(orginaltitel)
                                istzitatid = None
                                zitat = entities["CitCon"][zitattitelid]
                                hatzitatid = dql.suchePublikationsId(orginaltitel)
                                istzitatid = dql.suchePublikationsId(titelentities["DN"])
                                print(hatzitatid)
                                print(istzitatid)
                                print(zitat[0][:100])
                                if istzitatid != None:
                                    inst.insertPublikation_hat_Zitat(hatzitatid,istzitatid,zitat[0][:399])

                            except Exception as e:
                                print(e)
                                print("Kein Titel gefunden")
                except:
                    print("Kein Zitat gefunden")


parseZitate()