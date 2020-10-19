import psycopg2
import Daten.MAG as mag
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~üöä1234567890'''

def zitateAusgeben():
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    cur = con.cursor()
    sql = '''SELECT *  FROM Publikation_hat_Zitat;'''
    cur.execute(sql)
    ret = cur.fetchall()
    print(ret)
    con.commit()
    con.close

def topDreiNamenAusgaben():
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    cur = con.cursor()
    sql = '''SELECT Name , COUNT(Key) as Anzahl FROM AUTOR
        GROUP BY Name
        ORDER BY COUNT(Key) DESC 
        LIMIT 3;'''
    cur.execute(sql)
    ret = cur.fetchall()
    print(ret)
    con.commit()
    con.close

def suchePublikationsId(titel):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    cur = con.cursor()
    sql = '''SELECT ID FROM Publikation 
    WHERE TITEL ILIKE %s
    LIMIT 1;'''
    cur.execute(sql, (titel, ))
    ret = cur.fetchall()[0][0]
    print(ret)
    con.commit()
    con.close
    return ret

def zweihundertpublikation():
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    cur = con.cursor()
    sql = '''SELECT Titel FROM Publikation LIMIT 200;'''
    cur.execute(sql)
    ret = cur.fetchall()
    con.commit()
    con.close
    return ret