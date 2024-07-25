import requests
from datetime import datetime
from tkinter import *

def getweather():
    user_api = "0a21e6ff77036e1b21452afab8bf01d5"
    location = location_entry.get()
    
    if not location:
        T.insert(END, "Enter city name.\n")
        return

    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()

    if api_data['cod'] == '404':
        T.insert(END, f"Invalid city: {location}, please check your city name.\n")
        return

    # Create variables to store and display data
    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    weather_report = (
        f"-------------------------------------------------------------\n"
        f"Weather Stats for - {location.upper()}  || {date_time}\n"
        f"-------------------------------------------------------------\n"
        f"Current temperature is: {temp_city:.2f} deg C\n"
        f"Current weather desc  : {weather_desc}\n"
        f"Current Humidity      : {hmdt}%\n"
        f"Current wind speed    : {wind_spd} kmph\n"
    )

    T.insert(END, weather_report + '\n')

# GUI setup
root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")

l = Label(root, text="TODAY'S WEATHER REPORT:")
l.config(font=("Courier", 14))
l.pack()

location_entry = Entry(root)
location_entry.pack()

get_weather_button = Button(root, text="Get Weather", command=getweather)
get_weather_button.pack()

T = Text(root, height=20, width=60)
T.pack()

root.mainloop()
