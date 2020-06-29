# -*- coding: utf-8 -*-
"""
Weather Widget

Created on Sat Jun 27 16:36:13 2020

@author: ecwal
"""
import tkinter as tk
import requests
from open_weather_key import api_key

def get_weather() :
    """Looks up current weather from openweather.org,
    retrieves json and extracts location, weather conditions and temperature,
    then resets widget label text to display results.
    Look-up location taken from text entry box in widget loop below.

    Returns
    -------
    None.

    """
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"appid": api_key, "q": entry.get(), "units": "metric"}
    if entry.get() != "" :
        try :
            response = requests.get(url, params=params)
            data = response.json()
            weather = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            name = data["name"]
            label["text"] = "The weather in {} is {}\nThe temperature is {} C".format(name, weather, temp)
        except :
            label["text"] = "Sorry, I don't recognise that place."

#Widget loop:
root = tk.Tk()

canvas = tk.Canvas(root, height=50, width=200)
canvas.pack()

entry = tk.Entry(root)
entry.place(relx=0, rely=0)

label = tk.Label(root, text="")
label.pack(side="right")

button = tk.Button(root, text="Check", command=get_weather)
button.place(relx=0.8, rely=0)

root.mainloop()