import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

SECRET_KEY = os.getenv('SECRET_KEY')
DB_URI = os.getenv('DB_URI')

print('secret:', SECRET_KEY)
print('db uri:', DB_URI)

app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
db = SQLAlchemy(app)
