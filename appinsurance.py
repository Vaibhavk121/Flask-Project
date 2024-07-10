from flask import Flask, render_template
import pymysql

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '1234',
    'database': 'Insurance'
}

def get_db_connection():
    connection = pymysql.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database']
    )
    return connection

@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("select * from insurancedesc; ")
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('/Insurances/Insurances.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
