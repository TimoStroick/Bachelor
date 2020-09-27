import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")

print("Database opened successfully")

cur = con.cursor()

cur.execute('''DROP TABLE IF EXISTS AUTHOR CASCADE;''')
con.commit()
cur.execute('''CREATE TABLE AUTHOR
      (KEY CHAR(100) PRIMARY KEY     NOT NULL,
      NAME       CHAR(100)        NOT NULL);
      ''')
print("Table created successfully")
con.commit()

cur.execute('''DROP TABLE IF EXISTS PUBLIKATION CASCADE;''')
con.commit()
cur.execute('''CREATE TABLE PUBLIKATION
      (ID SERIAL PRIMARY KEY NOT NULL, 
      KEY CHAR(50)  ,
      TITEL           CHAR(300)     NOT NULL);''')
print("Table created successfully")
con.commit()

cur.execute('''DROP TABLE IF EXISTS AUTHOR_SCHREIBT_PUBLIKATION CASCADE;''')
con.commit()
cur.execute('''CREATE TABLE AUTHOR_SCHREIBT_PUBLIKATION
      (KEY CHAR(100)     NOT NULL,
      ID INTEGER       NOT NULL,
      PRIMARY KEY(KEY,ID),
      FOREIGN KEY(KEY) REFERENCES AUTHOR(KEY)
      ON DELETE CASCADE ON UPDATE CASCADE,
      FOREIGN KEY(ID) REFERENCES PUBLIKATION(ID)
      ON DELETE CASCADE ON UPDATE CASCADE);
      ''')
print("Table created successfully")
con.commit()

cur.execute('''DROP TABLE IF EXISTS ELEKTRONISCHE_VERSION CASCADE;''')
con.commit()
cur.execute('''CREATE TABLE ELEKTRONISCHE_VERSION
      (ADRESSE CHAR(100) PRIMARY KEY     NOT NULL,
      PublikationID           INTEGER     NOT NULL,
      FOREIGN KEY(PublikationID) REFERENCES PUBLIKATION(ID)
      ON DELETE CASCADE ON UPDATE CASCADE);
      ''')
print("Table created successfully")
con.commit()

cur.execute('''DROP TABLE IF EXISTS HOMEPAGE CASCADE;''')
con.commit()
cur.execute('''CREATE TABLE HOMEPAGE
      (ID SERIAL PRIMARY KEY  NOT NULL,
      URL CHAR(100)              ,
      TITEL     CHAR(200)            NOT NULL,
      NOTIZ     TEXT );
      ''')
print("Table created successfully")
con.commit()

cur.execute('''DROP TABLE IF EXISTS KONFERENZ CASCADE;''')
con.commit()
cur.execute('''CREATE TABLE KONFERENZ
      (ID SERIAL PRIMARY KEY    NOT NULL,
      TITEL         CHAR(100)   NOT NULL,
      BUCHTITEL     CHAR(100)   NOT NULL,
      JAHR          INT         NOT NULL,
      AUFLAGE       CHAR(50)    NOT NULL);''')
print("Table created successfully")
con.commit()

cur.execute('''DROP TABLE IF EXISTS FACHZEITSCHRIFT CASCADE;''')
con.commit()
cur.execute('''CREATE TABLE FACHZEITSCHRIFT
      (ID SERIAL PRIMARY KEY    NOT NULL,
      NAME          CHAR(100)   NOT NULL,
      URL           CHAR(100),
      JAHR          INT         NOT NULL,
      SEITEN        CHAR(25)    NOT NULL,
      AUFLAGE       CHAR(50)    NOT NULL);''')
print("Table created successfully")
con.commit()

cur.execute('''DROP TABLE IF EXISTS BUCH CASCADE;''')
con.commit()
cur.execute('''CREATE TABLE BUCH
      (ID SERIAL PRIMARY KEY    NOT NULL,
      TITEL         CHAR(100)   NOT NULL,
      JAHR          INT         NOT NULL,
      PUBLISHER     CHAR(50)    NOT NULL);''')
print("Table created successfully")
con.commit()

cur.execute('''DROP TABLE IF EXISTS BEARBEITER CASCADE;''')
con.commit()
cur.execute('''CREATE TABLE BEARBEITER
      (KEY CHAR(100) PRIMARY KEY     NOT NULL,
      NAME       CHAR(100)    NOT NULL);
      ''')
print("Table created successfully")
con.commit()

cur.execute('''DROP TABLE IF EXISTS Publikation_hat_Zitat CASCADE;''')
con.commit()
cur.execute('''CREATE TABLE Publikation_hat_Zitat
      (HatZitatID INTEGER      NOT NULL,
      IstZitiertID INTEGER      NOT NULL,
      PRIMARY KEY(HatZitatID,IstZitiertID),
      FOREIGN KEY(HatZitatID) REFERENCES PUBLIKATION(ID)
      ON DELETE CASCADE ON UPDATE CASCADE,
      FOREIGN KEY(IstZitiertID) REFERENCES PUBLIKATION(ID)
      ON DELETE CASCADE ON UPDATE CASCADE);
      ''')
print("Table created successfully")
con.commit()

cur.execute('''DROP TABLE IF EXISTS Author_hat_Homepage CASCADE;''')
con.commit()
cur.execute('''CREATE TABLE Author_hat_Homepage
      (AuthorKey CHAR(50)     NOT NULL,
      HomepageId INT     NOT NULL,
      PRIMARY KEY(AuthorKey,HomepageId),
      FOREIGN KEY(AuthorKey) REFERENCES AUTHOR(Key)
      ON DELETE CASCADE ON UPDATE CASCADE,
      FOREIGN KEY(HomepageId) REFERENCES HOMEPAGE(Id)
      ON DELETE CASCADE ON UPDATE CASCADE);
      ''')
print("Table created successfully")
con.commit()

cur.execute('''DROP TABLE IF EXISTS Bearbeiter_bearbeitet_Konferenz CASCADE;''')
con.commit()
cur.execute('''CREATE TABLE Bearbeiter_bearbeitet_Konferenz
      (BearbeiterKey CHAR(100)       NOT NULL,
      KonferenzId INT       NOT NULL,
      PRIMARY KEY(BearbeiterKey,KonferenzId),
      FOREIGN KEY(BearbeiterKey) REFERENCES BEARBEITER(Key)
      ON DELETE CASCADE ON UPDATE CASCADE,
      FOREIGN KEY(KonferenzId) REFERENCES KONFERENZ(Id)
      ON DELETE CASCADE ON UPDATE CASCADE);
      ''')
print("Table created successfully")
con.commit()

cur.execute('''DROP TABLE IF EXISTS Publikation_ist_in_Konferenz CASCADE;''')
con.commit()
cur.execute('''CREATE TABLE Publikation_ist_in_Konferenz
      (PublikationID INT      NOT NULL,
      KonferenzId INT       NOT NULL,
      PRIMARY KEY(PublikationID,KonferenzId),
      FOREIGN KEY(PublikationID) REFERENCES PUBLIKATION(ID)
      ON DELETE CASCADE ON UPDATE CASCADE,
      FOREIGN KEY(KonferenzId) REFERENCES KONFERENZ(Id)
      ON DELETE CASCADE ON UPDATE CASCADE);
      ''')
print("Table created successfully")
con.commit()

cur.execute('''DROP TABLE IF EXISTS Publikation_ist_in_Fachzeitschrift CASCADE;''')
con.commit()
cur.execute('''CREATE TABLE Publikation_ist_in_Fachzeitschrift
      (PublikationID INT       NOT NULL,
      FachzeitschriftId INT       NOT NULL,
      PRIMARY KEY(PublikationID,FachzeitschriftId),
      FOREIGN KEY(PublikationID) REFERENCES PUBLIKATION(ID)
      ON DELETE CASCADE ON UPDATE CASCADE,
      FOREIGN KEY(FachzeitschriftId) REFERENCES FACHZEITSCHRIFT(Id)
      ON DELETE CASCADE ON UPDATE CASCADE);
      ''')
print("Table created successfully")
con.commit()

cur.execute('''DROP TABLE IF EXISTS Publikation_ist_in_Buch CASCADE;''')
con.commit()
cur.execute('''CREATE TABLE Publikation_ist_in_Buch
      (PublikationID INT      NOT NULL,
      BuchId INT       NOT NULL,
      PRIMARY KEY(PublikationID,BuchId),
      FOREIGN KEY(PublikationID) REFERENCES PUBLIKATION(ID)
      ON DELETE CASCADE ON UPDATE CASCADE,
      FOREIGN KEY(BuchId) REFERENCES BUCH(Id)
      ON DELETE CASCADE ON UPDATE CASCADE);
      ''')
print("Table created successfully")
con.commit()

con.close()