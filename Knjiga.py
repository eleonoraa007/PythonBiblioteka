from mysql.connector import connect, Error
def unosKnjige():
    naziv = input("Unesi naziv knjige: ")
    kategorija = input("Unesi kategoriju: ")
    autor = input("Unesi autora: ")
    primerak = input("Unesite broj primeraka za datu knjigu: ")
    biblioteka = 1
    insert_knjiga_query = """
    INSERT INTO knjiga(naziv, kategorija, autor, primerak_idPrimerak, biblioteka_idbiblioteka)
    VALUES(%s, %s, %s, %s, %s);
    """ 
    val_tuple = (
        naziv,
        kategorija,
        autor,
        primerak,
        biblioteka
    )
    try:
        with connect(
            host="localhost",
            user="root",
            password="root",
            database="biblioteka",
        ) as connection:
            with connection.cursor() as cursor:
                for result in cursor.execute(insert_knjiga_query, val_tuple, multi=True):
                    if result.with_rows:
                        print(result.fetchall())
                connection.commit()
                print('Dodata je nova knjiga: ' + naziv)
    except Error as e:
        print(e)

def delete():
    naziv1 = input("Unesite naziv Knjige: ")
    delete_query = """
        DELETE FROM knjiga WHERE naziv = '%s';  
    """ % (naziv1)
    try:
        with connect(
            host="localhost",
            user="root",
            password="root",
            database="biblioteka",
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(delete_query)
                connection.commit()
    except Error as e:
        print(e)

def ispis():
    conn = connect(host='localhost', password='root', user='root', database='biblioteka')
    mycursor = conn.cursor()
    mycursor.execute("select naziv from knjiga")
    for i in mycursor:
        print(i[0])

def ispis2():
    conn = connect(host='localhost', password='root', user='root', database='biblioteka')
    mycursor = conn.cursor()
    mycursor.execute("select distinct kategorija from knjiga")
    for i in mycursor:
        print(i)

def ispisKnjigaPremaZanru():
    kategorija = input("Unesite zeljenu kategoriju: ")
    insert_kat_query = """
    SELECT naziv FROM knjiga WHERE kategorija = '%s';
    """ % (kategorija)
    try:
        with connect(
            host="localhost",
            user="root",
            password="root",
            database="biblioteka",
        ) as connection:
            with connection.cursor() as cursor:
                for result in cursor.execute(insert_kat_query, multi=True):
                    if result.with_rows:
                        print(result.fetchall())
                connection.commit()
    except Error as e:
        print(e) 

def main():
    unesi = input("Da li zelite da unesete knjigu? Da/Ne ")
    if unesi == 'Da':
        unosKnjige()
    izbrisi = input("Da li zelite da izbrisete knjigu? Da/Ne ")
    if izbrisi == 'Da':
        print("Data vam je lista knjiga iz koje mozete da izbrisete zeljenu knjigu: ")
        ispis()
        delete()
    ispisZanra = input("Da li zelite da prikazete knjige odredjenog zanra? Da/Ne ")
    if ispisZanra == 'Da':
        print("Data vam je lista svih kategorija: ") 
        ispis2()
        ispisKnjigaPremaZanru()

main()