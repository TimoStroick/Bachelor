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
    return ret

def readAttribute(end):
    global f
    global line
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
        print("fail :" + ret)
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
            break
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
        else:
            print(list)
            print("elsepath")
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
    print(taglist)

def parseProceeding(taglist):
    global f
    global line
    print(taglist)

def parseBook(taglist):
    global f
    global line
    print(taglist)

def parseIncollection(taglist):
    global f
    global line
    print(taglist)

def parsePhdthesis(taglist):
    global f
    global line
    print(taglist)

def parseMasterthesis(taglist):
    global f
    global line
    print(taglist)

def parseWww(taglist):
    global f
    global line
    print(taglist)
