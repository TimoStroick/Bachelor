import Datenbank.Funktionen as fkt
global f
global line

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

    print(ret)
    return ret

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
        print(ret)
        return ret

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
            print("--->parseArticle(list)")
            parseArticle(list)
        elif 0 <= list[0].find("inproceedings"):
            print("--->parseInproceedings(list)")
            parseInproceedings(list)
        elif 0 <= list[0].find("proceeding"):
            print("--->parseProceeding(list)")
            parseProceeding(list)
        elif 0 <= list[0].find("book"):
            print("--->parseBook(list)")
            parseBook(list)
        elif 0 <= list[0].find("incollection"):
            print("--->parseIncollection(list)")
            parseIncollection(list)
        elif 0 <= list[0].find("phdthesis"):
            print("--->parsePhdthesis(list)")
            parsePhdthesis(list)
        elif 0 <= list[0].find("masterthesis"):
            print("--->parseMasterthesis(list)")
            parseMasterthesis(list)
        elif 0 <= list[0].find("www"):
            print("--->parseWww(list)")
            parseWww(list)
        elif 0 <= list[0].find("/dblp"):
            print("end")
            break
        else:
            print(list)
            print("elsepath")

        line = line.strip()
        if len(line) == 0:
            line = f.readline()


def parseArticle(taglist):
    global f
    global line
    author = []
    ee = []
    title = ""
    year = 0
    journal = ""
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
        elif 0 <= attr[0].find("title"):
            title = attr[1]
        elif 0 <= attr[0].find("year"):
            year = attr[1]
        elif 0 <= attr[0].find("journal"):
            journal = attr[1]
        else:
            print(attr[0] + " : " + attr[1])
    fkt.insertPublikation(title, year, author, ee, journal)
    print("<---parseArticle")

def parseInproceedings(taglist):
    global f
    global line
    line = line.strip()
    if 1 > len(line):
        line = f.readline()
    a = 1
    while a:
        attr = readAttribute("inproceedings")
        if 0 <= attr[0].find("/inproceedings"):
            line = line[line.find(">"):]
            a = 0
        else:
            print(attr[0] + " : " + attr[1])

    print("<---parseInproceedings")

def parseProceeding(taglist):
    global f
    global line
    line = line.strip()
    if 1 > len(line):
        line = f.readline()
    a = 1
    while a:
        attr = readAttribute("proceeding")
        if 0 <= attr[0].find("/proceeding"):
            line = line[line.find(">"):]
            a = 0
        else:
            print(attr[0] + " : " + attr[1])

    print("<---parseProceeding")

def parseBook(taglist):
    global f
    global line
    line = line.strip()
    if 1 > len(line):
        line = f.readline()
    a = 1
    while a:
        attr = readAttribute("book")
        if 0 <= attr[0].find("/book"):
            line = line[line.find(">"):]
            a = 0
        else:
            print(attr[0] + " : " + attr[1])

    print("<---parseBook")

def parseIncollection(taglist):
    global f
    global line
    line = line.strip()
    if 1 > len(line):
        line = f.readline()
    a = 1
    while a:
        attr = readAttribute("incollection")
        if 0 <= attr[0].find("/incollection"):
            line = line[line.find(">"):]
            a = 0
        else:
            print(attr[0] + " : " + attr[1])

    print("<---parseIncollection")

def parsePhdthesis(taglist):
    global f
    global line
    line = line.strip()
    if 1 > len(line):
        line = f.readline()
    a = 1
    while a:
        attr = readAttribute("phdthesis")
        if 0 <= attr[0].find("/phdthesis"):
            line = line[line.find(">"):]
            a = 0
        else:
            print(attr[0] + " : " + attr[1])

    print("<---parsePhdthesis")

def parseMasterthesis(taglist):
    global f
    global line
    line = line.strip()
    if 1 > len(line):
        line = f.readline()
    a = 1
    while a:
        attr = readAttribute("masterthesis")
        if 0 <= attr[0].find("/masterthesis"):
            line = line[line.find(">"):]
            a = 0
        else:
            print(attr[0] + " : " + attr[1])

    print("<---parseMasterthesis")

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
    fkt.insertHomepage(title, author)

    print("<---parseArticle")
