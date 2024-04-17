from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Function to connect to the MySQL database
def connect_db():
    return mysql.connector.connect(
        host='your_mysql_host',
        user='your_mysql_username',
        password='your_mysql_password',
        database='your_mysql_database'
    )

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the query form submission
@app.route('/query', methods=['POST'])
def query():
    query_result = None
    query = request.form['query']
    
    # Connect to the MySQL database
    db = connect_db()
    cursor = db.cursor()
    
    try:
        cursor.execute(query)
        query_result = cursor.fetchall()
    except mysql.connector.Error as e:
        query_result = str(e)
    
    db.close()
    
    return render_template('query_result.html', query=query, result=query_result)

if __name__ == '__main__':
    app.run(debug=True)
