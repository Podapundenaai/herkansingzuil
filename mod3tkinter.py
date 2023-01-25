import tkinter
from tkinter import *
import psycopg2
import requests
from PIL import Image, ImageTk

root = Tk()
#import database
con = psycopg2.connect(
        host = "localhost",
        database = "projectzuil",
        user = "postgres",
        password = "pundenaai")
con.autocommit = True

#Add NS Logo
image = Image.open('images/nslogopunde.png')
image = image.resize((100,50), Image.LANCZOS)
logo= ImageTk.PhotoImage(image)
canvas = Label(root, image=logo)
canvas.pack(anchor='n')

root.config(bg='#c2ab00')
#Api Key
api_key = "776769430a770b9cf165c5011a73fe4c"

#Root URL
root_url = "http://api.openweathermap.org/data/2.5/weather?"

#Plaats
city = "Utrecht"

#URL
url = f"{root_url}appid={api_key}&q={city}&lang=NL&units=metric'"

#URL opvragen
r = requests.get(url)

#Api Key
data = r.json()

#Aanvraag vanuit API
if data['cod'] == 200:
    temperatuur = data['main']['temp'] #Kelvin
    temp = round(temperatuur - 273.15) #Convert to Celcius
    beschrijving = data['weather'][0]['description']
    wind = data['wind']['speed']

    print(f"Plaats: {city}")
    print(f"Weer conditie: {beschrijving}")
    print(f"Temperatuur: {temp}")
    print(f"Snelheid van wind: {wind} m/s")
else:
    print("Er is wat fout gegaan!")

#Label Station
bestemming = Label(master=root,
              text= f"Wij verwelkomen u bij Station: {city}",
              background='#c2ab00',
              foreground='black',
              font=('Futura', 20, 'bold italic'))

#Label stad
stad = Label(master=root,
              text= f"Plaats: {city}",
              background='#c2ab00',
              foreground='black',
              font=('Futura', 16, 'italic'))

#Label weerconditie
conditie = Label(master=root,
              text= f"Conditie van het weer: {beschrijving}",
              background='#c2ab00',
              foreground='black',
              font=('Futura', 16, 'italic'))

#label Temperature
temperature = Label(master=root,
              text= f"Temperatuur: {temp}℃",
              background='#c2ab00',
              foreground='black',
              font=('Futura', 16, 'italic'))

#label windkracht
kracht = Label(master=root,
              text= f"Windkracht: {wind} m/s",
              background='#c2ab00',
              foreground='black',
              font=('Futura', 16, 'italic'))

temperature.pack(anchor='nw') #Tonen van de label
conditie.pack(anchor='nw') #Tonen van de label
kracht.pack(anchor='nw') #Tonen van de label
stad.pack(anchor='nw') #Tonen van de label
def station():
   con = psycopg2.connect(
   host='localhost', database="projectzuil", user='postgres', password='pundenaai')
   con.autocommit = True
   cursor = con.cursor()
   cursor.execute('''SELECT * from station_service where station_city = 'Utrecht' ''')
   result = cursor.fetchone();



   con.commit()
   con.close()
   return result

station()

service = station()

ov_bike = 'zijn aanwezig' if service[2] else 'niet aanwezig'
elevator = 'aanwezig' if service[3] else 'niet aanwezig'
toilet = 'zijn aanwezig' if service[4] else 'niet aanwezig'
park_and_ride = 'open' if service[5] else 'gesloten'


ov_bike_label = Label(master=root,
              text= "OV-fiets(en): "+ ov_bike,
              background='#c2ab00',
              foreground='#4f4f00',
              font=('Helvetica', 16, 'bold italic'))

elevator_label = Label(master=root,
              text= "Lift: "+ elevator,
              background='#c2ab00',
              foreground='#4f4f00',
              font=('Helvetica', 16, 'bold italic'))

toilet_label = Label(master=root,
              text= "Toilet: "+ toilet,
              background='#c2ab00',
              foreground='#4f4f00',
              font=('Helvetica', 16, 'bold italic'))

park_and_ride_label = Label(master=root,
              text= "Park and Ride: "+ park_and_ride,
              background='#c2ab00',
              foreground='#4f4f00',
              font=('Helvetica', 16, 'bold italic'))

ov_bike_label.pack(anchor='e')
elevator_label.pack(anchor='e')
toilet_label.pack(anchor='e')
park_and_ride_label.pack(anchor='e')




berichten = [] #Lege list

def messages(): #Functie om berichten te tonen van heel NL
    cursor = con.cursor()
    query = """SELECT bericht_id, moderator_id, tekst, datum, tijd
           FROM bericht 
           ORDER BY bericht_id DESC
           LIMIT 5 ;"""
    cursor.execute(query)
    records = cursor.fetchall()
    cursor.close()
    for record in records:
        berichten.append(str(record[2]))
    return berichten

#Per bericht tonen
for bericht in messages():
    label = Label(master=root,
              text= f"{bericht}",
              background='#c2ab00',
              foreground='#4f4f00',
              font=('montserrat', 18))
    label.pack(anchor='center')


root.geometry("600x400")
# label.pack()

bestemming.pack(anchor='s') #Tonen van de label


con.close()

root.mainloop()