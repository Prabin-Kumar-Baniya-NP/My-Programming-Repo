import requests
import json
from tkinter import *


def getweather():
    url = "http://api.openweathermap.org/data/2.5/weather?"
    api_key = "0c6d92daecea782cc14db6a6d92e4e8b"
    location = city_name.get()
    complete_url = url + "q=" + location + "&APPID=" + api_key
    response = requests.get(complete_url)
    x = response.json()
    p = x["cod"]
    if p != "404":
        print(x)
        y = x["main"]
        a = x["weather"]
        b = a[0]['main']
        c = a[0]['description']
        temperature = y["temp"]
        max_temp = y["temp_max"]
        min_temp = y["temp_min"]
        global output1, output2, output3, output4, output5
        output1 = Label(root, text="Weather condition  : " + b)
        output2 = Label(root, text="Weather description: " + c)
        output3 = Label(root, text="Minimum Temperature: %.3f degree Celsius" % (min_temp - 273))
        output4 = Label(root, text="Maximum Temperature: %.2f degree Celsius" % (temperature - 273))
        output5 = Label(root, text="Average Temperature: %.3f degree Celsius" % (max_temp - 273))
        clear = Button(root, text="CLEAR", command=all_clear1)
        output1.grid(row=3)
        output2.grid(row=4)
        output3.grid(row=5)
        output4.grid(row=6)
        output5.grid(row=7)
        clear.grid(row=8)

    else:
        global output_error
        clear = Button(root, text="CLEAR", command=all_clear2)
        output_error = Label(root, text="Invalid City name \n Try again")
        clear.grid(row=8)
        output_error.grid(row=3)

def all_clear1():
    city_name.delete(0,END)
    output1.grid_remove()
    output2.grid_remove()
    output3.grid_remove()
    output4.grid_remove()
    output5.grid_remove()

def all_clear2():
    output_error.grid_remove()


# create a window
root = Tk()
root.title("Get Weather")
header = Label(root, text="Welcome to Weather Application")
button1 = Button(root, text="Enter city name", width=15, borderwidth=5)
button2 = Button(root, text="Search", height=1, fg="blue", command=getweather)
city_name = Entry(root)
city_name.grid(row=1, column=1)
button1.grid(row=1, column=0)
button2.grid(row=2, column=0, padx=10, pady=10)
header.grid(row=0, column=0)
root.mainloop()
