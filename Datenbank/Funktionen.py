import psycopg2


def saveProceedings(editors, ees, title, series, auflage, jahr, url, buchtitel, isbn, publisher):
    konferenzid = insertKonferenz(title, buchtitel, jahr, auflage)
    for editor in editors:
        editor = editor.strip()
        insertBearbeiter(editor)
        insertBearbeiter_bearbeitet_Konferenz(editor,konferenzid)
    print("Saved")


def saveInproceedings(authors, ees, title, seiten, auflage, jahr, url, crossref, buchtitel):
    publikationid = insertPublikation(title)
    for author in authors:
        author = author.strip()
        insertAuthor(author)
        insertAuthor_schreibt_Publikation(author, publikationid)
    for ee in ees:
        insertElektronischeVersion(ee, publikationid)
    konferenzid = insertKonferenz(title, buchtitel, jahr, auflage)
    buchid = insertBuch(buchtitel, jahr, "")
    insertPublikation_ist_in_Buch(publikationid, buchid)
    insertPublikation_ist_in_Konferenz(publikationid, konferenzid)
    print("Inproceeding Saved")


def saveIncollection(authors, title, ees, seiten, jahr, booktitel, crossref, url):
    publikationid = insertPublikation(title)
    for author in authors:
        author = author.strip()
        insertAuthor(author)
        insertAuthor_schreibt_Publikation(author, publikationid)
    for ee in ees:
        insertElektronischeVersion(ee, publikationid)
    buchid = insertBuch(booktitel, jahr, "")
    insertPublikation_ist_in_Buch(publikationid, buchid)
    print("Incollection Saved")


def saveArticle(title, year, authors, ees, journal, volume, number, pages, cite):
    publikationid = insertPublikation(title)
    for author in authors:
        author = author.strip()
        insertAuthor(author)
        insertAuthor_schreibt_Publikation(author, publikationid)
    for ee in ees:
        insertElektronischeVersion(ee,publikationid)
    fachzeitschriftid = insertFachzeitschrift(journal, "", year, pages, volume)
    insertPublikation_ist_in_Fachzeitschrift(publikationid,fachzeitschriftid)
    print("Article Saved")


def saveBuch(author, ees, title, jahr, isbn, publisher, series):
    insertBuch(title, jahr, publisher)
    print("Buch Saved")


def saveHomepage(title, authors, note, url):
    homepageid = insertHomepage(title, note, url)
    for author in authors:
        author = author.strip()
        insertAuthor(author)
        insertAuthor_hat_Homepage(author, homepageid)
    print("Homepage Saved")


def saveMasterthesis():
    print("Saved")


def savePhdthesis():
    print("Saved")


def insertPublikation(titel):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    cur = con.cursor()
    sql = '''INSERT INTO PUBLIKATION (TITEL)
                    VALUES (%s) RETURNING ID;
                  '''
    cur.execute(sql, (titel, ))
    ret = cur.fetchone()[0]
    print("Table created successfully")
    con.commit()
    return ret


def insertAuthor(key):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    print(key)
    key = key.strip()
    list = key.split(" ")
    name = ""
    if isinstance(list[-1], int):
        for x in list[:-2]:
            name = name + " " + x
    else:
        for x in list:
            name = name + " " + x
    name = name.strip()
    try:
        cur = con.cursor()
        sql = '''INSERT INTO AUTHOR (KEY, NAME)
                    VALUES (%s,%s);
                 '''
        cur.execute(sql, (key, name, ))
        con.commit()
        print("Author Saved")
    except:
        print("Author bereits vorhanden")



def insertAuthor_schreibt_Publikation(key,id):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    cur = con.cursor()
    sql = '''INSERT INTO AUTHOR_SCHREIBT_PUBLIKATION (KEY,ID)
                        VALUES (%s,%s);
                      '''
    cur.execute(sql, (key, id, ))
    con.commit()
    print("Author_schreibt_Publikation Saved")


def insertBearbeiter(key):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    key = key.strip()
    list = key.split(" ")
    name = ""
    if isinstance(list[-1], int):
        for x in list[:-1]:
            name = name + " " + x
    else:
        for x in list:
            name = name + " " + x
    name = name.strip()
    print(name)
    try:
        cur = con.cursor()
        sql = '''INSERT INTO BEARBEITER (KEY, NAME)
                    VALUES (%s,%s);
                 '''
        cur.execute(sql, (key, name, ))
        con.commit()
        print("Bearbeiter Saved")
    except:
        print("Bearbeiter bereits vorhanden")


def insertHomepage(titel, notiz, url):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    cur = con.cursor()
    sql = '''INSERT INTO HOMEPAGE (titel, notiz, url)
                            VALUES (%s,%s,%s)
                            RETURNING ID;
                          '''
    cur.execute(sql, (titel, notiz, url, ))
    ret = cur.fetchone()[0]
    con.commit()
    print("Saved")
    return ret


def insertAuthor_hat_Homepage(author, id):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    cur = con.cursor()
    sql = '''INSERT INTO Author_hat_Homepage (AuthorKey, HomepageId)
                                VALUES (%s,%s);
                              '''
    cur.execute(sql, (author.strip(), id, ))
    con.commit()
    print("Saved")


def insertBuch(titel, jahr, publisher):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    cur = con.cursor()
    try:
        sql = '''SELECT ID FROM BUCH
                    WHERE TITEL = %s AND
                    JAHR = %s ;'''
        cur.execute(sql, (titel, jahr,))
        con.commit()
        ret = cur.fetchall()[0][0]
        print("Buch gefunden")
        print(ret)
    except :
        sql = '''INSERT INTO BUCH (TITEL, JAHR, PUBLISHER)
                                        VALUES (%s,%s,%s)
                                        RETURNING ID;
                                      '''
        cur.execute(sql, (titel, jahr, publisher, ))
        ret = cur.fetchone()[0]
        con.commit()
        print("Buch Saved")
    return ret


def insertKonferenz(titel, buchtitel, jahr, auflage):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    cur = con.cursor()
    try:
        sql = '''SELECT ID FROM KONFERENZ
                WHERE TITEL = %s AND
                BUCHTITEL = %s AND
                JAHR = %s ;'''
        cur.execute(sql, (titel, buchtitel, jahr,))
        ret = cur.fetchall()[0][0]
        con.commit()
        print("Saved")
    except:
        sql = '''INSERT INTO KONFERENZ (TITEL, BUCHTITEL, JAHR, AUFLAGE)
                                            VALUES (%s,%s,%s,%s)
                                            RETURNING ID;'''
        cur.execute(sql, (titel, buchtitel, jahr, auflage, ))
        ret = cur.fetchone()[0]
        con.commit()
        print("Saved")
    return ret


def insertFachzeitschrift(name, url, jahr, seiten, auflage):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    cur = con.cursor()
    sql = '''INSERT INTO FACHZEITSCHRIFT (NAME, URL, JAHR, SEITEN, AUFLAGE)
                                            VALUES (%s,%s,%s,%s,%s)
                                            RETURNING ID;
                                          '''
    cur.execute(sql, (name, url, jahr, seiten, auflage, ))
    ret = cur.fetchone()[0]
    con.commit()
    print("Saved")
    return ret


def insertElektronischeVersion(adresse, id):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    try:
        cur = con.cursor()
        sql = '''INSERT INTO ELEKTRONISCHE_VERSION (ADRESSE, PUBLIKATIONID)
                                                   VALUES (%s,%s);'''
        cur.execute(sql, (adresse, id, ))
        print("Table created successfully")
        con.commit()
        print("Saved")
    except:
        print("ee schon gespeichert")


def insertPublikation_hat_Zitat(hatzitatId, istzitatId):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    cur = con.cursor()
    sql = '''INSERT INTO Publikation_hat_Zitat (HatZitatID, IstZitiertID)
                                                VALUES (%s,%s);'''
    cur.execute(sql, (hatzitatId, istzitatId, ))
    con.commit()
    print("Saved")


def insertBearbeiter_bearbeitet_Konferenz(bearbeiterKey, konferenzId):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    cur = con.cursor()
    sql = '''INSERT INTO Bearbeiter_bearbeitet_Konferenz (BearbeiterKey, KonferenzId)
                                                VALUES (%s,%s);'''
    cur.execute(sql, (bearbeiterKey, konferenzId, ))
    con.commit()
    print("Saved")


def insertPublikation_ist_in_Konferenz(publikationID, konferenzId):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    cur = con.cursor()
    sql = '''INSERT INTO Publikation_ist_in_Konferenz (PublikationID, KonferenzId)
                                                VALUES (%s,%s);'''
    cur.execute(sql, (publikationID, konferenzId, ))
    con.commit()
    print("Saved")


def insertPublikation_ist_in_Fachzeitschrift(publikationID, fachzeitschriftId):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    cur = con.cursor()
    sql = '''INSERT INTO Publikation_ist_in_Fachzeitschrift (PublikationID, FachzeitschriftId)
                                                VALUES (%s,%s);'''
    cur.execute(sql, (publikationID, fachzeitschriftId, ))
    con.commit()
    print("Saved")


def insertPublikation_ist_in_Buch(publikationID, buchId):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    cur = con.cursor()
    sql = '''INSERT INTO Publikation_ist_in_Buch (PublikationID, BuchId)
                                                VALUES (%s,%s);'''
    cur.execute(sql, (publikationID, buchId, ))
    con.commit()
    print("Saved")

def insertZitat(hatZitat,istZitat):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    cur = con.cursor()
    sql = '''INSERT INTO Publikation_hat_Zitat (HatZitatID, IstZitiertID)
                                                    VALUES (%s,%s);'''
    cur.execute(sql, (hatZitat, istZitat,))
    con.commit()
    print("Saved")