#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Warning", "Enter city name!")
        return
    
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=bd5e378503939ddaee76f12ad7a97608&units=metric"
        data = requests.get(url).json()
        
        if data.get('cod') == 200:
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            result_label.config(text=f"{city}: {temp}°C, {desc}")
        else:
            result_label.config(text="City not found!")
    except:
        result_label.config(text="Error! Check internet")

# Create window
root = tk.Tk()
root.title("RAj Weather")
root.geometry("400x200")

# Widgets
tk.Label(root, text="RAj Weather", font=('Arial', 20)).pack(pady=10)
city_entry = tk.Entry(root, font=('Arial', 14))
city_entry.pack(pady=5)
tk.Button(root, text="Get Weather", command=get_weather).pack(pady=5)
result_label = tk.Label(root, text="", font=('Arial', 12))
result_label.pack(pady=10)

root.mainloop()