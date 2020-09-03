import psycopg2

def saveProceedings(editor, ee, title, series, volume, year, url, booktitle, isbn, publisher):
    print("Saved")

def saveInproceedings():
    print("Saved")

def saveIncollection():
    print("Saved")

def savePublikation(title, year, author, ee, journal, volume, number, pages, cite):
    print("Saved")

def insertPublikation(title, year, author, ee, journal, cite):
    print("Saved")

def insertAuthor(key):
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
    print("Database opened successfully")
    key = key.strip()
    list = key.split(" ")
    if list[-1].is_integer():
        for x in list[:-1]:
            name = name + " " + x
    else:
        for x in list:
            name = name + " " + x
    name = name.strip()

    cur = con.cursor()
    cur.execute('''INSERT INTO AUTHOR (KEY, NAME)
                VALUES ('''+ key +","+ name +''');
              ''')
    print("Table created successfully")
    con.commit()
    print("Saved")

def insertBearbeiter():
    print("Saved")

def insertHomepage(title, author, note, url):
    print("Saved")

def insertBuch():
    print("Saved")

def insertKonferenz():
    print("Saved")

def insertFachzeitschrift():
    print("Saved")

def insertElektronischeVersion():
    print("Saved")
