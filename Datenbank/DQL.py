import psycopg2
import Daten.MAG as mag
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~üöä1234567890'''

con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
cur = con.cursor()
sql = '''SELECT Titel FROM Publikation LIMIT 1;'''
cur.execute(sql)
ret = cur.fetchall()
con.commit()
con.close




def suchePublikationsId(titel):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    cur = con.cursor()
    sql = '''SELECT ID FROM Publikation 
    WHERE TITEL ILIKE %s
    LIMIT 1;'''
    cur.execute(sql, (titel, ))
    ret = cur.fetchall()[0]
    print(ret)
    con.commit()
    con.close
    return ret

def hundertpublikation():
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    cur = con.cursor()
    sql = '''SELECT Titel FROM Publikation LIMIT 1;'''
    cur.execute(sql)
    ret = cur.fetchall()
    con.commit()
    con.close
    return ret
    for row in ret:
       titel = row[0]
       for ele in titel:
           if ele in punc:
               titel = titel.replace(ele, "")

       titel = titel.lower()
       titel = titel.strip()
       print(titel)
       mag.sucheZitate(titel)