import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'cities.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db, render_as_batch=True)

class City(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    population = db.Column(db.Integer)
    country = db.Column(db.String(100), nullable=False)
    first_mentioned = db.Column(db.String(50))



    def __init__(self, name, population, country, first_mentioned):
        self.name = name
        self.population = population
        self.country = country
        self.first_mentioned = first_mentioned


    def __repr__(self):
        return f'{self.name}, country: {self.country}, population: {self.population}, first mentioned: {self.first_mentioned}'
