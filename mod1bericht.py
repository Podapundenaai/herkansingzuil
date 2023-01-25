import random
from datetime import datetime
import psycopg2
import psycopg2.extras

con = psycopg2.connect(
        host = "localhost",
        database = "projectzuil",
        user = "postgres",
        password = "pundenaai")

con.autocommit = True

datum = datetime.now().date().strftime("%d/%m/%Y")
tijd = datetime.now().time().strftime("%H:%M:%S")

reiziger = input("Wat is uw naam? of wilt u anoniem blijven")
if reiziger == "":
    print("Uw naam is anoniem")
else:
    print('Hallo', reiziger)

infile = open(
    'stations.txt').read().splitlines()
rstation = random.choice(infile)
print(rstation)
lijnen = open('tekst.csv', 'r')

while True:
    bericht = input('Voer hier uw bericht in (max 140 karakters): ')
    if len(bericht) <= 140:
        print('Uw bericht wordt doorgestuurd naar de moderator, Fijne dag nog!')
        break
    else: print('Opnieuw graag! Uw bericht heeft teveel karakters')

file = open('tekst.csv', 'a')
file.write(f"{reiziger}, {rstation}, {datum}, {tijd}, {bericht}\n")


con.commit()
con.close()
