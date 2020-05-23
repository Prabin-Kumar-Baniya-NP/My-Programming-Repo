from flask import Flask, render_template
import datetime
import requests
import json
app = Flask(__name__)


@app.route('/')
def hello():
    todays_date=datetime.datetime.now()
    new_year=todays_date.month==1 and todays_date.day==1
    return render_template("index.html", my_var="Hi Prabin",new_year=new_year)
@app.route('/contact')
def contact_me():
    name="Prabin Kumar Baniya"
    email="pra44bin@gmail.com"
    return render_template('contact.html', name=name, email=email)
@app.route('/more')
def more():
    message="If you like our service please contact us"
    return render_template()

@app.route('/weather')
def getweather():
    url = "http://api.openweathermap.org/data/2.5/weather?"
    api_key = "0c6d92daecea782cc14db6a6d92e4e8b"
    location="Butwal"
    complete_url= url + "q=" + location + "&APPID=" + api_key
    response=requests.get(complete_url)
    x=response.json()
    return x
