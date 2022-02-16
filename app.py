from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///home/dante/Documents/dantesblog/data.db'

db = SQLAlchemy(app)


@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('about')
def about ():
    return render_template('about.html')

@app.route('contact')
def contact():
    return render_template('contact.html')

if __name__=='__main__':
    app.run(debug=True)