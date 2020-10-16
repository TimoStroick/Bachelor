import Datenbank.Einfügen as inst


def saveProceedings(editors, ees, titel, series, auflage, jahr, url, buchtitel, isbn, herausgeber):
    konferenzid = inst.insertKonferenz(titel, buchtitel, jahr, auflage, series, herausgeber)
    inst.insertISBN(isbn)
    inst.insertKonferenz_hat_ISBN(isbn, konferenzid)
    for editor in editors:
        editor = editor.strip()
        inst.insertAutor(editor)
        inst.insertAutor_bearbeitet_Konferenz(editor, konferenzid)
    for ee in ees:
        inst.insertElektronischeVersion(ee)
        inst.insertKonferenz_hat_ElektronischeVersion(ee, konferenzid)
    print("Saved")


def saveInproceedings(authors, ees, titel, seiten, auflage, jahr, url, crossref, buchtitel, serie, herausgeber):
    publikationid = inst.insertPublikation(titel, jahr, "")
    for author in authors:
        author = author.strip()
        inst.insertAutor(author)
        inst.insertAutor_schreibt_Publikation(author, publikationid)
    for ee in ees:
        inst.insertElektronischeVersion(ee)
        inst.insertPublikation_hat_ElektronischeVersion(ee, publikationid)
    konferenzid = inst.insertKonferenz(titel, buchtitel, jahr, auflage, serie, herausgeber)
    inst.insertPublikation_ist_in_Konferenz(publikationid, konferenzid, seiten)
    print("Inproceeding Saved")


def saveIncollection(authors, titel, ees, seiten, jahr, buchtitel, crossref, url):
    publikationid = inst.insertPublikation(titel, jahr, "")
    for author in authors:
        author = author.strip()
        inst.insertAutor(author)
        inst.insertAutor_schreibt_Publikation(author, publikationid)
    for ee in ees:
        inst.insertElektronischeVersion(ee)
        inst.insertPublikation_hat_ElektronischeVersion(ee, publikationid)
    buchid = inst.insertBuch(buchtitel, jahr, "","","")
    inst.insertPublikation_ist_in_Buch(publikationid, buchid, seiten)
    print("Incollection Saved")


def saveArticle(titel, jahr, authors, ees, fachzeitschrift, auflage, seiten, cite, herausgeber):
    publikationid = inst.insertPublikation(titel, jahr, "")
    for author in authors:
        author = author.strip()
        inst.insertAutor(author)
        inst.insertAutor_schreibt_Publikation(author, publikationid)
    for ee in ees:
        inst.insertElektronischeVersion(ee)
        inst.insertPublikation_hat_ElektronischeVersion(ee, publikationid)
    fachzeitschriftid = inst.insertFachzeitschrift(fachzeitschrift, "", jahr, auflage, herausgeber)
    inst.insertPublikation_ist_in_Fachzeitschrift(publikationid, fachzeitschriftid, seiten)
    print("Article Saved")


def saveBook(authors, ees, titel, jahr, isbn, herausgeber, series, auflage):
    buchid = inst.insertBuch(titel, jahr, herausgeber, auflage, series)
    for author in authors:
        author = author.strip()
        inst.insertAutor(author)
        inst.insertAutor_schreibt_Buch(author, buchid)
    for ee in ees:
        inst.insertElektronischeVersion(ee)
        inst.insertBuch_hat_ElektronischeVersion(ee, buchid)
    for nummer in isbn:
        inst.insertElektronischeVersion(nummer)
        inst.insertBuch_hat_ISBN(nummer, buchid)
    print("Buch Saved")


def saveHomepage(titel, authors, note, url):
    inst.insertHomepage(titel, note, url)
    for author in authors:
        author = author.strip()
        inst.insertAutor(author)
        inst.insertAuthor_hat_Homepage(author, url)
    print("Homepage Saved")


def saveMasterthesis(titel, authors, jahr, universitaet, ees, note):
    publikationid = inst.insertPublikation(titel, jahr, universitaet)
    for author in authors:
        author = author.strip()
        inst.insertAutor(author)
        inst.insertAutor_schreibt_Publikation(author, publikationid)
    for ee in ees:
        inst.insertElektronischeVersion(ee)
        inst.insertPublikation_hat_ElektronischeVersion(ee, publikationid)
    print("Saved")


def savePhdthesis(titel, authors, jahr, seiten, herausgeber, series, auflage, universitaet, isbn, ees):
    publikationid = inst.insertPublikation(titel, jahr, universitaet)
    buchid = inst.insertBuch(titel, jahr, herausgeber, auflage, series)
    for author in authors:
        author = author.strip()
        inst.insertAutor(author)
        inst.insertAutor_schreibt_Publikation(author, publikationid)
    for ee in ees:
        inst.insertElektronischeVersion(ee)
        inst.insertPublikation_hat_ElektronischeVersion(ee, publikationid)
    for nummer in isbn:
        inst.insertElektronischeVersion(nummer)
        inst.insertBuch_hat_ISBN(nummer, buchid)
    inst.insertPublikation_ist_in_Buch(publikationid, buchid, seiten)
    print("Saved")