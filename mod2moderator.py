import datetime
from datetime import datetime
import csv
import psycopg2
import psycopg2.extras
from tkinter import *

#Connect to the database
con = psycopg2.connect(
        host = "localhost",
        database = "projectzuil",
        user = "postgres",
        password = "pundenaai")

con.autocommit = True

#Function om moderator toe te voegen
def moderator_insert():
    cursor = con.cursor()

    mod_name = input('Wat is uw naam?')
    mod_email = input('Wat is uw e-mailadres?')
    time = datetime.now().time().strftime("%H:%M:%S")
    date = datetime.now().date().strftime("%Y/%m/%d")

    query = """
            INSERT INTO moderator (datum, tijd, naam, email)
            VALUES (%s, %s, %s, %s);
            """

    cursor.execute(query, (date, time, mod_name, mod_email,))
    cursor.close()

#Execute
moderator_insert()

#Function om berichten toe te voegen
def insert_berichten():
    cursor = con.cursor()

    with open('goedgekeurd.csv', 'r') as goedgekeurd_csv:
        csv_reader = csv.reader(goedgekeurd_csv, delimiter=',')
        for row in csv_reader:
            mod_id = 19
            date = datetime.now().date().strftime("%Y/%m/%d")
            time = datetime.now().time().strftime("%H:%M:%S")
            tekst = row[4]

            query = """
                    INSERT INTO bericht(moderator_id, tekst, datum, tijd)
                    VALUES (%s, %s, %s, %s)
                    """

            cursor.execute(query, (mod_id, tekst, date, time))


#Goedkeuring vragen
with open('tekst.csv', 'r') as bestand_csv:
    csv_reader = csv.reader(bestand_csv, delimiter=',')

    for row in csv_reader:
        tekst = row[4]
        goedgekeurd = input(f"Wordt het volgende bericht goedgekeurd?\n "
                            f"{tekst}\n "
                            f"ja/nee: ")

        if goedgekeurd == 'ja':
            file = open('goedgekeurd.csv', 'a')
            file.write(f"{', '.join(row)}\n")
            file.close()
        elif goedgekeurd == 'nee':
            file2 = open('afgekeurd.csv', 'a')
            file2.write(f"{', '.join(row)}\n")
            file2.close()

    verwijder = open('tekst.csv', 'w')
    verwijder.write('')
    verwijder.close()

    #Als het goed gekeurd is moet ie de functie uitvoeren
    insert_berichten()

    o = open('goedgekeurd.csv', "w+")
    o.close()

    print("Alle openstaande berichten zijn toegevoegd/afgekeurd!")

    con.commit()
