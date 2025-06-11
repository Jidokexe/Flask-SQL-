from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
# Конфигурация подключения из переменных окружения
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/users')
def get_users():
    users = User.query.all()
    return jsonify([u.name for u in users])
