from flask import render_template
from . import mysql

def home():
    return render_template('index.html')

def users():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM Users")
    data = cursor.fetchall()
    cursor.close()
    return render_template('users.html', users=data)

# Registering routes with the Flask app
def register_routes(app):
    app.add_url_rule('/', 'home', home)
    app.add_url_rule('/users', 'users', users)
