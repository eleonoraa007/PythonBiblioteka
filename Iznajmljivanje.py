from mysql.connector import connect, Error
def iznajmljenaKnjiga():
    iznajmljena = """
    SELECT datum, COUNT(idIznajmljuje) AS knjige
    FROM biblioteka.iznajmljuje
    GROUP BY datum;
    """
    conn = connect(host='localhost', password='root', user='root', database='biblioteka')
    mycursor = conn.cursor()
    mycursor.execute(iznajmljena)
    for datum, broj_knjiga in mycursor:
        print("Broj iznajmljenih knjiga na dan", datum,"je:",broj_knjiga)

def clan():
    primerci = """
    SELECT 
	c.ime, 
    COUNT(i.primerak_idPrimerak) AS broj_iznajmljenih_knjiga,
    DATE_FORMAT(i.datum, "%m-%Y") AS mesec_iznajmljivanja
    FROM biblioteka.clan c
    INNER JOIN biblioteka.iznajmljuje i
    WHERE c.idclan = i.clan_idclan
    GROUP BY
	c.ime,
    mesec_iznajmljivanja,
    MONTH(mesec_iznajmljivanja),
    YEAR(mesec_iznajmljivanja);
    """
    conn = connect(host='localhost', password='root', user='root', database='biblioteka')
    mycursor = conn.cursor()
    mycursor.execute(primerci)
    for ime, broj_knjiga, datum in mycursor:
        print("Broj iznajmljenih knjiga za clana",ime,"za mesec", datum,"je:",broj_knjiga)


def main():
    print("Prikazi sledece: ")
    unos = input("(1.)Broj iznajmljenih knjiga po danima \n(2.)Broj iznajmljenih knjiga za jednog člana po mesecima \n")
    if unos == "1" or unos == "1.":
        iznajmljenaKnjiga()
    if unos == "2" or unos == "2.":
        print("Ispis: ")
        clan()
    

main()