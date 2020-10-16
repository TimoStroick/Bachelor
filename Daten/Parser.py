import Datenbank.DBParser as fkt
global f
global line

# readTag(tag)
# tag = Alles was in den Klammern steht "<",">"
# return = Eine Liste wo eintrag 0 der Name des Tags ist. Danach immer Attribut und Attributwert
def readTag(tag):

    taglist = tag.split(" ")
    ret = [taglist[0]]
    i = 1
    while i < len(taglist):
        tmp = taglist[i]
        if 0 < tmp.find("="):
            ret.append(tmp[0:tmp.find("=")])
            ret.append(tmp[(tmp.find("=")+1):-1])
        else:
            print(tmp)
        i = i+1

    return ret

# readAttribute(end)
# end = Ist das Endtag von dem Tag wo die Unterpunkte herausgefunden werden
# return = eine Liste mit Eintrag 0 = Nametag und 1 = Wert
def readAttribute(end):
    global f
    global line
    if line == "\n":
        print("newline")
        line = f.readline()
    list = readTag(line[(line.find("<") + 1):line.find(">")])
    ret = [list[0]]

    if list[0].find("/"+end) >= 0:
        return ret
    ret.append(line[(line.find(">") + 1):line.rfind("<")])
    line = line[(line.rfind("<") + 1):]
    if 0 <= line.find("/"):
        line = line[(line.rfind(">") + 1):]
        line = line.strip()
        if 1 > len(line):
            line = f.readline()
        return ret
    else:
        return ret


# startparser(dateipfad)
# dateipfad = Welche Datei soll eingelesen werden
# Hier wird Tag nach Tag überprüft und jenach Tag ein Fall ausgewählt
# return = void
def startparser(dateipfad):
    global f
    global line
    f = open(dateipfad, "r")
    line = f.readline()
    a = 1
    while a:
        list = readTag(line[(line.find("<")+1):line.find(">")])
        line = line[(line.find(">")+1):]
        if 0 <= list[0].find("article"):
            parseArticle(list)
        elif 0 <= list[0].find("inproceedings"):
            parseInproceedings(list)
        elif 0 <= list[0].find("proceeding"):
            parseProceeding(list)
        elif 0 <= list[0].find("book"):
            parseBook(list)
        elif 0 <= list[0].find("incollection"):
            parseIncollection(list)
        elif 0 <= list[0].find("phdthesis"):
            parsePhdthesis(list)
        elif 0 <= list[0].find("masterthesis"):
            parseMasterthesis(list)
        elif 0 <= list[0].find("www"):
            parseWww(list)
        elif 0 <= list[0].find("/dblp"):
            print("end")
            break
        else:
            print(list)
            #print("elsepath")

        line = line.strip()
        if len(line) == 0:
            line = f.readline()


def parseArticle(taglist):
    global f
    global line
    author = []
    ee = []
    cite = []
    title = ""
    year = 0
    journal = ""
    volume = ""
    publisher = ""
    pages = ""
    line = line.strip()
    if 1 > len(line):
        line = f.readline()
    a = 1
    while a:
        attr = readAttribute("article")
        if 0 <= attr[0].find("/article"):
            line = line[line.find(">"):]
            a = 0
        elif 0 <= attr[0].find("author"):
            author.append(attr[1])
        elif 0 <= attr[0].find("ee"):
            ee.append(attr[1])
        elif 0 <= attr[0].find("cite"):
            cite.append(attr[1])
        elif 0 <= attr[0].find("title"):
            title = attr[1]
        elif 0 <= attr[0].find("year"):
            year = attr[1]
        elif 0 <= attr[0].find("volume"):
            volume = attr[1]
        elif 0 <= attr[0].find("pages"):
            pages = attr[1]
        elif 0 <= attr[0].find("journal"):
            journal = attr[1]
        elif 0 <= attr[0].find("publisher"):
            publisher = attr[1]
        else:
            print(attr[0] + " : " + attr[1])
    fkt.saveArticle(title, year, author, ee, journal, volume, pages, cite, publisher)

def parseInproceedings(taglist):
    global f
    global line
    author = []
    ee = []
    title = ""
    pages = ""
    year = 0
    booktitle = ""
    volume = ""
    url = ""
    crossref = ""
    serie = ""
    publisher = ""
    line = line.strip()
    if 1 > len(line):
        line = f.readline()
    a = 1
    while a:
        attr = readAttribute("inproceedings")
        if 0 <= attr[0].find("/inproceedings"):
            line = line[line.find(">"):]
            a = 0
        elif 0 <= attr[0].find("author"):
            author.append(attr[1])
        elif 0 <= attr[0].find("ee"):
            ee.append(attr[1])
        elif 0 <= attr[0].find("title"):
            title = attr[1]
        elif 0 <= attr[0].find("pages"):
            pages = attr[1]
        elif 0 <= attr[0].find("volume"):
            volume = attr[1]
        elif 0 <= attr[0].find("year"):
            year = attr[1]
        elif 0 <= attr[0].find("url"):
            url = attr[1]
        elif 0 <= attr[0].find("crossref"):
            crossref = attr[1]
        elif 0 <= attr[0].find("booktitle"):
            booktitle = attr[1]
        elif 0 <= attr[0].find("publisher"):
            publisher = attr[1]
        elif 0 <= attr[0].find("serie"):
            serie = attr[1]
        else:
            print(attr[0] + " : " + attr[1])

    fkt.saveInproceedings(author, ee, title, pages, volume, year, url, crossref, booktitle, serie, publisher)

def parseProceeding(taglist):
    global f
    global line
    editor = []
    ee = []
    title = ""
    booktitle = ""
    series = ""
    volume = 0
    year = 0
    url = ""
    isbn = ""
    publisher = ""
    line = line.strip()
    if 1 > len(line):
        line = f.readline()
    a = 1
    while a:
        attr = readAttribute("proceeding")
        if 0 <= attr[0].find("/proceeding"):
            line = line[line.find(">"):]
            a = 0
        elif 0 <= attr[0].find("editor"):
            editor.append(attr[1])
        elif 0 <= attr[0].find("ee"):
            ee.append(attr[1])
        elif 0 <= attr[0].find("title"):
            title = attr[1]
        elif 0 <= attr[0].find("series"):
            series = attr[1]
        elif 0 <= attr[0].find("volume"):
            volume = attr[1]
        elif 0 <= attr[0].find("year"):
            year = attr[1]
        elif 0 <= attr[0].find("url"):
            url = attr[1]
        elif 0 <= attr[0].find("booktitle"):
            booktitle = attr[1]
        elif 0 <= attr[0].find("isbn"):
            isbn = attr[1]
        elif 0 <= attr[0].find("publisher"):
            publisher = attr[1]
        else:
            print(attr[0] + " : " + attr[1])
    fkt.saveProceedings(editor, ee, title, series, volume, year, url, booktitle, isbn, publisher)

def parseBook(taglist):
    global f
    global line
    author = []
    ee = []
    title = ""
    year = 0
    isbn = []
    publisher = ""
    series = ""
    volume = 0
    line = line.strip()
    if 1 > len(line):
        line = f.readline()
    a = 1
    while a:
        attr = readAttribute("book")
        if 0 <= attr[0].find("/book"):
            line = line[line.find(">"):]
            a = 0
        elif 0 <= attr[0].find("author"):
            author.append(attr[1])
        elif 0 <= attr[0].find("ee"):
            ee.append(attr[1])
        elif 0 <= attr[0].find("title"):
            title = attr[1]
        elif 0 <= attr[0].find("year"):
            year = attr[1]
        elif 0 <= attr[0].find("isbn"):
            isbn.append(attr[1])
        elif 0 <= attr[0].find("publisher"):
            publisher = attr[1]
        elif 0 <= attr[0].find("series"):
            series = attr[1]
        elif 0 <= attr[0].find("volume"):
            volume = attr[1]
        else:
            print(attr[0] + " : " + attr[1])
    fkt.saveBook(author, ee, title, year, isbn, publisher, series, volume)


def parseIncollection(taglist):
    global f
    global line
    author = []
    ee = []
    title = ""
    pages = ""
    year = 0
    booktitle = ""
    url = ""
    crossref = ""
    line = line.strip()
    if 1 > len(line):
        line = f.readline()
    a = 1
    while a:
        attr = readAttribute("incollection")
        if 0 <= attr[0].find("/incollection"):
            line = line[line.find(">"):]
            a = 0
        elif 0 <= attr[0].find("author"):
            author.append(attr[1])
        elif 0 <= attr[0].find("ee"):
            ee.append(attr[1])
        elif 0 <= attr[0].find("title"):
            title = attr[1]
        elif 0 <= attr[0].find("pages"):
            pages = attr[1]
        elif 0 <= attr[0].find("year"):
            year = attr[1]
        elif 0 <= attr[0].find("booktitle"):
            booktitle = attr[1]
        elif 0 <= attr[0].find("crossref"):
            crossref = attr[1]
        elif 0 <= attr[0].find("url"):
            url = attr[1]
        else:
            print(attr[0] + " : " + attr[1])

    fkt.saveIncollection(author, title, ee, pages, year, booktitle, crossref, url)

def parsePhdthesis(taglist):
    global f
    global line
    author = []
    ee = []
    isbn = []
    title = ""
    pages = ""
    school = ""
    publisher = ""
    series = ""
    volume = 0
    year = 0
    line = line.strip()
    if 1 > len(line):
        line = f.readline()
    a = 1
    while a:
        attr = readAttribute("phdthesis")
        if 0 <= attr[0].find("/phdthesis"):
            line = line[line.find(">"):]
            a = 0
        elif 0 <= attr[0].find("author"):
            author.append(attr[1])
        elif 0 <= attr[0].find("ee"):
            ee.append(attr[1])
        elif 0 <= attr[0].find("isbn"):
            isbn.append(attr[1])
        elif 0 <= attr[0].find("title"):
            title = attr[1]
        elif 0 <= attr[0].find("school"):
            school = attr[1]
        elif 0 <= attr[0].find("pages"):
            pages = attr[1]
        elif 0 <= attr[0].find("publisher"):
            publisher = attr[1]
        elif 0 <= attr[0].find("series"):
            series = attr[1]
        elif 0 <= attr[0].find("volume"):
            volume = attr[1]
        elif 0 <= attr[0].find("year"):
            year = attr[1]
        else:
            print(attr[0] + " : " + attr[1])

    fkt.savePhdthesis(title, author, year, pages, publisher, series, volume, school, isbn, ee)

def parseMasterthesis(taglist):
    global f
    global line
    author = []
    ee = []
    title = ""
    note = ""
    year = 0
    school = ""
    line = line.strip()
    if 1 > len(line):
        line = f.readline()
    a = 1
    while a:
        attr = readAttribute("masterthesis")
        if 0 <= attr[0].find("/masterthesis"):
            line = line[line.find(">"):]
            a = 0
        elif 0 <= attr[0].find("author"):
            author.append(attr[1])
        elif 0 <= attr[0].find("ee"):
            ee.append(attr[1])
        elif 0 <= attr[0].find("title"):
            title = attr[1]
        elif 0 <= attr[0].find("school"):
            school = attr[1]
        elif 0 <= attr[0].find("year"):
            year = attr[1]
        else:
            print(attr[0] + " : " + attr[1])

    fkt.saveMasterthesis(title, author, year, school, ee, note)

def parseWww(taglist):
    global f
    global line
    author = []
    url = []
    note = []
    title = ""
    line = line.strip()
    if 1 > len(line):
        line = f.readline()
    a = 1
    while a:
        attr = readAttribute("www")
        if 0 <= attr[0].find("/www"):
            line = line[line.find(">"):]
            a = 0
        elif 0 <= attr[0].find("author"):
            author.append(attr[1])
        elif 0 <= attr[0].find("url"):
            url.append(attr[1])
        elif 0 <= attr[0].find("note"):
            note.append(attr[1])
        elif 0 <= attr[0].find("title"):
            title = attr[1]
        else:
            print(attr[0] + " : " + attr[1])
    fkt.saveHomepage(title, author, note, url)

