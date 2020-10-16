import psycopg2



def insertPublikation(titel, jahr, universitaet):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    cur = con.cursor()
    sql = '''INSERT INTO PUBLIKATION (TITEL,JAHR,UNIVERSITAET)
                    VALUES (%s,%s,%s) RETURNING ID;
                  '''
    cur.execute(sql, (titel, jahr, universitaet, ))
    ret = cur.fetchone()[0]
    con.commit()
    return ret


def insertAutor(key):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    key = key.strip()
    list = key.split(" ")
    name = key
    for i in list:
        if i.isdigit():
            name = key[0:key.find(i)]
    name = name.strip()
    try:
        cur = con.cursor()
        sql = '''INSERT INTO AUTOR (KEY, NAME)
                    VALUES (%s,%s);
                 '''
        cur.execute(sql, (key, name, ))
        con.commit()
    except Exception as e:
        print(e)
        print("Author bereits vorhanden")



def insertAutor_schreibt_Publikation(key,id):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    cur = con.cursor()
    sql = '''INSERT INTO AUTOR_SCHREIBT_PUBLIKATION (KEY,ID)
                        VALUES (%s,%s);
                      '''
    cur.execute(sql, (key, id, ))
    con.commit()


def insertHomepage(titel, notiz, url):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    try:
        cur = con.cursor()
        sql = '''INSERT INTO HOMEPAGE (titel, notiz, url)
                                    VALUES (%s,%s,%s);
                                  '''
        cur.execute(sql, (titel, notiz, url,))
        con.commit()
    except:
        print("Hompage bereits vorhanden")
    return url


def insertAuthor_hat_Homepage(autor, url):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    try:
        cur = con.cursor()
        sql = '''INSERT INTO Autor_hat_Homepage (AutorKey, URL)
                                    VALUES (%s,%s);
                                  '''
        cur.execute(sql, (autor.strip(), url, ))
        con.commit()

    except:
        print("Autor_hat_Homepage schon vorhanden")


def insertBuch(titel, jahr, herausgeber, auflage, serie):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    cur = con.cursor()
    try:
        sql = '''SELECT ID FROM BUCH
                    WHERE TITEL = %s AND
                    JAHR = %s ;'''
        cur.execute(sql, (titel, jahr,))
        con.commit()
        ret = cur.fetchall()[0][0]
    except :
        sql = '''INSERT INTO BUCH (TITEL, JAHR, Herausgeber, Auflage, serie)
                                        VALUES (%s,%s,%s,%s,%s)
                                        RETURNING ID;
                                      '''
        cur.execute(sql, (titel, jahr, herausgeber, auflage, serie))
        ret = cur.fetchone()[0]
        con.commit()
    return ret


def insertKonferenz(titel, buchtitel, jahr, auflage, serie, herausgeber):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    cur = con.cursor()
    try:
        sql = '''SELECT ID FROM KONFERENZ
                WHERE TITEL = %s AND
                BUCHTITEL = %s AND
                JAHR = %s AND
                serie = %s ;'''
        cur.execute(sql, (titel, buchtitel, jahr, serie, ))
        ret = cur.fetchall()[0][0]
        con.commit()
    except:
        sql = '''INSERT INTO KONFERENZ (TITEL, BUCHTITEL, JAHR, AUFLAGE, serie, herausgeber)
                                            VALUES (%s,%s,%s,%s,%s,%s)
                                            RETURNING ID;'''
        cur.execute(sql, (titel, buchtitel, jahr, auflage, serie, herausgeber, ))
        ret = cur.fetchone()[0]
        con.commit()
    return ret


def insertFachzeitschrift(name, url, jahr, auflage, herausgeber):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    cur = con.cursor()
    sql = '''INSERT INTO FACHZEITSCHRIFT (NAME, URL, JAHR, AUFLAGE, herausgeber)
                                            VALUES (%s,%s,%s,%s,%s)
                                            RETURNING ID;
                                          '''
    cur.execute(sql, (name, url, jahr, auflage, herausgeber, ))
    ret = cur.fetchone()[0]
    con.commit()
    return ret


def insertElektronischeVersion(adresse):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    try:
        cur = con.cursor()
        sql = '''INSERT INTO ELEKTRONISCHE_VERSION (ADRESSE)
                                    VALUES (%s);'''
        cur.execute(sql, (adresse, ))
        con.commit()
    except:
        print("ee schon gespeichert")

def insertPublikation_hat_ElektronischeVersion(adresse, publikationsid):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    try:
        cur = con.cursor()
        sql = '''INSERT INTO Publikation_hat_ELEKTRONISCHEVERSION (ADRESSE, Publikationid)
                                    VALUES (%s);'''
        cur.execute(sql, (adresse, publikationsid, ))
        con.commit()
    except:
        print("ee schon gespeichert")

def insertBuch_hat_ElektronischeVersion(adresse, buchid):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    try:
        cur = con.cursor()
        sql = '''INSERT INTO BUCH_hat_ELEKTRONISCHEVERSION (ADRESSE, BuchID)
                                    VALUES (%s,%s);'''
        cur.execute(sql, (adresse, buchid, ))
        con.commit()
    except:
        print("ee schon gespeichert")

def insertKonferenz_hat_ElektronischeVersion(adresse, konferenzid):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    try:
        cur = con.cursor()
        sql = '''INSERT INTO BUCH_hat_ELEKTRONISCHEVERSION (ADRESSE, KonferenzID)
                                    VALUES (%s,%s);'''
        cur.execute(sql, (adresse, konferenzid, ))
        con.commit()
    except:
        print("ee schon gespeichert")


def insertISBN(isbn):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    try:
        cur = con.cursor()
        sql = '''INSERT INTO ISBN (ISBN)
                                    VALUES (%s);'''
        cur.execute(sql, (isbn, ))
        con.commit()
    except:
        print("ee schon gespeichert")


def insertBuch_hat_ISBN(isbn, buchid):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    try:
        cur = con.cursor()
        sql = '''INSERT INTO BUCH_hat_ISBN (isbn, BuchID)
                                    VALUES (%s,%s);'''
        cur.execute(sql, (isbn, buchid,))
        con.commit()
    except:
        print("ee schon gespeichert")


def insertKonferenz_hat_ISBN(isbn, konferenzid):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    try:
        cur = con.cursor()
        sql = '''INSERT INTO Konferenz_hat_ISBN (isbn, KonferenzID)
                                    VALUES (%s,%s);'''
        cur.execute(sql, (isbn, konferenzid,))
        con.commit()
    except:
        print("ee schon gespeichert")


def insertPublikation_hat_Zitat(hatzitatId, istzitatId, zitat):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    cur = con.cursor()
    sql = '''INSERT INTO Publikation_hat_Zitat (HatZitatID, IstZitiertID,zitat)
                                                VALUES (%s,%s,%s);'''
    cur.execute(sql, (hatzitatId, istzitatId, zitat, ))
    con.commit()


def insertAutor_bearbeitet_Konferenz(key, konferenzId):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    cur = con.cursor()
    key = key.strip()
    sql = '''INSERT INTO Autor_bearbeitet_Konferenz (key, KonferenzId)
                                                VALUES (%s,%s);'''
    cur.execute(sql, (key, konferenzId, ))
    con.commit()

def insertAutor_schreibt_Buch(key, buchid):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    cur = con.cursor()
    key = key.strip()
    sql = '''INSERT INTO AUTOR_SCHREIBT_BUCH (key, id)
                                                VALUES (%s,%s);'''
    cur.execute(sql, (key, buchid, ))
    con.commit()

def insertPublikation_ist_in_Konferenz(publikationID, konferenzId, seiten):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    cur = con.cursor()
    sql = '''INSERT INTO Publikation_ist_in_Konferenz (PublikationID, KonferenzId, seiten)
                                                VALUES (%s,%s,%s);'''
    cur.execute(sql, (publikationID, konferenzId, seiten, ))
    con.commit()


def insertPublikation_ist_in_Fachzeitschrift(publikationID, fachzeitschriftId, seiten):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    cur = con.cursor()
    sql = '''INSERT INTO Publikation_ist_in_Fachzeitschrift (PublikationID, FachzeitschriftId, seiten)
                                                VALUES (%s,%s,%s);'''
    cur.execute(sql, (publikationID, fachzeitschriftId, seiten))
    con.commit()


def insertPublikation_ist_in_Buch(publikationID, buchId, seiten):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    cur = con.cursor()
    sql = '''INSERT INTO Publikation_ist_in_Buch (PublikationID, BuchId, seiten)
                                                VALUES (%s,%s,%s);'''
    cur.execute(sql, (publikationID, buchId, seiten))
    con.commit()
