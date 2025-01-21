from flask import Flask, render_template, request, redirect, url_for
import pyodbc

app = Flask(__name__)

# Database connection
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=<your_server>.database.windows.net;'
    'DATABASE=StudentDB;'
    'UID=<your_username>;'
    'PWD=<your_password>'
)
cursor = conn.cursor()

@app.route('/')
def home():
    return "Hello, Azure Flask App!"

# CRUD operations here...

if __name__ == '__main__':
    app.run(debug=True)
