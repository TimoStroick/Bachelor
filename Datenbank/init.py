import psycopg2
def initialisieren():
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")

    print("Database opened successfully")

    cur = con.cursor()

    cur.execute('''DROP TABLE IF EXISTS AUTOR CASCADE;''')
    con.commit()
    cur.execute('''CREATE TABLE AUTOR
          (KEY VARCHAR(100) PRIMARY KEY     NOT NULL,
          NAME       VARCHAR(100)        NOT NULL);
          ''')
    print("Table created successfully")
    con.commit()

    cur.execute('''DROP TABLE IF EXISTS PUBLIKATION CASCADE;''')
    con.commit()
    cur.execute('''CREATE TABLE PUBLIKATION
          (ID SERIAL PRIMARY KEY NOT NULL, 
          TITEL           VARCHAR(500)     NOT NULL,
          JAHR      INTEGER  NOT NULL,
          UNIVERSITAET VARCHAR(100));''')
    print("Table created successfully")
    con.commit()

    cur.execute('''DROP TABLE IF EXISTS AUTOR_SCHREIBT_PUBLIKATION CASCADE;''')
    con.commit()
    cur.execute('''CREATE TABLE AUTOR_SCHREIBT_PUBLIKATION
          (KEY VARCHAR(100)     NOT NULL,
          ID INTEGER       NOT NULL,
          PRIMARY KEY(KEY,ID),
          FOREIGN KEY(KEY) REFERENCES AUTOR(KEY)
          ON DELETE CASCADE ON UPDATE CASCADE,
          FOREIGN KEY(ID) REFERENCES PUBLIKATION(ID)
          ON DELETE CASCADE ON UPDATE CASCADE);
          ''')
    print("Table created successfully")
    con.commit()


    cur.execute('''DROP TABLE IF EXISTS ELEKTRONISCHE_VERSION CASCADE;''')
    con.commit()
    cur.execute('''CREATE TABLE ELEKTRONISCHE_VERSION
          (ADRESSE VARCHAR(100) PRIMARY KEY     NOT NULL);
          ''')
    print("Table created successfully")
    con.commit()


    cur.execute('''DROP TABLE IF EXISTS ISBN CASCADE;''')
    con.commit()
    cur.execute('''CREATE TABLE ISBN
              (ISBN VARCHAR(100) PRIMARY KEY     NOT NULL);
              ''')
    print("Table created successfully")
    con.commit()


    cur.execute('''DROP TABLE IF EXISTS HOMEPAGE CASCADE;''')
    con.commit()
    cur.execute('''CREATE TABLE HOMEPAGE
          (URL VARCHAR(200)   PRIMARY KEY  NOT NULL,
          TITEL     VARCHAR(200)            NOT NULL,
          NOTIZ     VARCHAR(500) );
          ''')
    print("Table created successfully")
    con.commit()


    cur.execute('''DROP TABLE IF EXISTS KONFERENZ CASCADE;''')
    con.commit()
    cur.execute('''CREATE TABLE KONFERENZ
          (ID SERIAL PRIMARY KEY    NOT NULL,
          TITEL         VARCHAR(100)   NOT NULL,
          BUCHTITEL     VARCHAR(100),
          JAHR          INT         NOT NULL,
          SERIE        VARCHAR(100),
          Auflage    VARCHAR(50),
          Herausgeber  VARCHAR(50));''')
    print("Table created successfully")
    con.commit()

    cur.execute('''DROP TABLE IF EXISTS FACHZEITSCHRIFT CASCADE;''')
    con.commit()
    cur.execute('''CREATE TABLE FACHZEITSCHRIFT
          (ID SERIAL PRIMARY KEY    NOT NULL,
          NAME          VARCHAR(100)   NOT NULL,
          URL           VARCHAR(100),
          JAHR          INT         NOT NULL,
          AUFLAGE       VARCHAR(50)    NOT NULL,
          Herausgeber   VARCHAR(100));''')
    print("Table created successfully")
    con.commit()

    cur.execute('''DROP TABLE IF EXISTS BUCH CASCADE;''')
    con.commit()
    cur.execute('''CREATE TABLE BUCH
          (ID SERIAL PRIMARY KEY    NOT NULL,
          TITEL         VARCHAR(100)   NOT NULL,
          JAHR          INT         NOT NULL,
          SERIE        VARCHAR(100),
          AUFLAGE    VARCHAR(50),
          Herausgeber  VARCHAR(50));''')
    print("Table created successfully")
    con.commit()

    cur.execute('''DROP TABLE IF EXISTS AUTOR_SCHREIBT_BUCH CASCADE;''')
    con.commit()
    cur.execute('''CREATE TABLE AUTOR_SCHREIBT_BUCH
              (KEY VARCHAR(100)     NOT NULL,
              ID INTEGER       NOT NULL,
              PRIMARY KEY(KEY,ID),
              FOREIGN KEY(KEY) REFERENCES AUTOR(KEY)
              ON DELETE CASCADE ON UPDATE CASCADE,
              FOREIGN KEY(ID) REFERENCES BUCH(ID)
              ON DELETE CASCADE ON UPDATE CASCADE);
              ''')
    print("Table created successfully")
    con.commit()

    cur.execute('''DROP TABLE IF EXISTS Publikation_hat_Zitat CASCADE;''')
    con.commit()
    cur.execute('''CREATE TABLE Publikation_hat_Zitat
          (HatZitatID INTEGER      NOT NULL,
          IstZitiertID INTEGER      NOT NULL,
          Zitat VARCHAR(400) NOT NULL,
          PRIMARY KEY(HatZitatID,IstZitiertID),
          FOREIGN KEY(HatZitatID) REFERENCES PUBLIKATION(ID)
          ON DELETE CASCADE ON UPDATE CASCADE,
          FOREIGN KEY(IstZitiertID) REFERENCES PUBLIKATION(ID)
          ON DELETE CASCADE ON UPDATE CASCADE);
          ''')
    print("Table created successfully")
    con.commit()

    cur.execute('''DROP TABLE IF EXISTS Autor_hat_Homepage CASCADE;''')
    con.commit()
    cur.execute('''CREATE TABLE Autor_hat_Homepage
          (AutorKey VARCHAR(50)     NOT NULL,
          URL VARCHAR(200)     NOT NULL,
          PRIMARY KEY(AutorKey,URL),
          FOREIGN KEY(AutorKey) REFERENCES AUTOR(Key)
          ON DELETE CASCADE ON UPDATE CASCADE,
          FOREIGN KEY(URL) REFERENCES HOMEPAGE(URL)
          ON DELETE CASCADE ON UPDATE CASCADE);
          ''')
    print("Table created successfully")
    con.commit()

    cur.execute('''DROP TABLE IF EXISTS Autor_bearbeitet_Konferenz CASCADE;''')
    con.commit()
    cur.execute('''CREATE TABLE Autor_bearbeitet_Konferenz
          (Key VARCHAR(100)       NOT NULL,
          KonferenzId INT       NOT NULL,
          PRIMARY KEY(Key,KonferenzId),
          FOREIGN KEY(Key) REFERENCES Autor(Key)
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
          Seiten VARCHAR(50),
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
          Seiten VARCHAR(50),
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
          Seiten VARCHAR(50),
          PRIMARY KEY(PublikationID,BuchId),
          FOREIGN KEY(PublikationID) REFERENCES PUBLIKATION(ID)
          ON DELETE CASCADE ON UPDATE CASCADE,
          FOREIGN KEY(BuchId) REFERENCES BUCH(Id)
          ON DELETE CASCADE ON UPDATE CASCADE);
          ''')
    print("Table created successfully")
    con.commit()

    cur.execute('''DROP TABLE IF EXISTS Publikation_hat_ELEKTRONISCHEVERSION CASCADE;''')
    con.commit()
    cur.execute('''CREATE TABLE Publikation_hat_ELEKTRONISCHEVERSION
              (ADRESSE VARCHAR(100) PRIMARY KEY     NOT NULL,
              PublikationID           INTEGER ,
              FOREIGN KEY(PublikationID) REFERENCES PUBLIKATION(ID)
              ON DELETE CASCADE ON UPDATE CASCADE);
              ''')
    print("Table created successfully")
    con.commit()

    cur.execute('''DROP TABLE IF EXISTS BUCH_hat_ELEKTRONISCHEVERSION CASCADE;''')
    con.commit()
    cur.execute('''CREATE TABLE BUCH_hat_ELEKTRONISCHEVERSION
                  (ADRESSE VARCHAR(100) PRIMARY KEY     NOT NULL,
                  BuchID           INTEGER ,
                  FOREIGN KEY(BuchID) REFERENCES BUCH(ID)
                  ON DELETE CASCADE ON UPDATE CASCADE);
                  ''')
    print("Table created successfully")
    con.commit()

    cur.execute('''DROP TABLE IF EXISTS Konferenz_hat_ELEKTRONISCHEVERSION CASCADE;''')
    con.commit()
    cur.execute('''CREATE TABLE Konferenz_hat_ELEKTRONISCHEVERSION
                  (ADRESSE VARCHAR(100) PRIMARY KEY     NOT NULL,
                  KonferenzID           INTEGER ,
                  FOREIGN KEY(KonferenzID) REFERENCES Konferenz(ID)
                  ON DELETE CASCADE ON UPDATE CASCADE);
                  ''')
    print("Table created successfully")
    con.commit()

    cur.execute('''DROP TABLE IF EXISTS BUCH_hat_ISBN CASCADE;''')
    con.commit()
    cur.execute('''CREATE TABLE BUCH_hat_ISBN
                      (ISBN VARCHAR(100) PRIMARY KEY     NOT NULL,
                      BuchID           INTEGER ,
                      FOREIGN KEY(BuchID) REFERENCES BUCH(ID)
                      ON DELETE CASCADE ON UPDATE CASCADE);
                      ''')
    print("Table created successfully")
    con.commit()

    cur.execute('''DROP TABLE IF EXISTS Konferenz_hat_ISBN CASCADE;''')
    con.commit()
    cur.execute('''CREATE TABLE Konferenz_hat_ISBN
                      (ISBN VARCHAR(100) PRIMARY KEY     NOT NULL,
                      KonferenzID           INTEGER ,
                      FOREIGN KEY(KonferenzID) REFERENCES Konferenz(ID)
                      ON DELETE CASCADE ON UPDATE CASCADE);
                      ''')
    print("Table created successfully")
    con.commit()

    con.close()