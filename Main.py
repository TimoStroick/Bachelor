import Daten.Parser as parser
import Datenbank.init as init

#Erst wird die Datenbank initialisiert
init.initialisieren()
#Dann geparst
parser.startparser(".\Dokumente\dblp.xml")
