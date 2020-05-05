from flask import Flask, render_template
import datetime
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
