from flask import Flask, jsonify, request
import sqlite3
from flask_cors import CORS

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/months', methods=['GET'])
def months():

    conn = sqlite3.connect('FreshFruit.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM months')
    results = cursor.fetchall()
    conn.close()

    months = []
    for row in results:
        month = {"id" : row[0], "name" : row[1], "abbreviation" : row[2]}
        months.append(month)

    return jsonify({'status': 'success', 'data' : {'months' : months}})


@app.route('/fruits', methods=['GET'])
def fruits():

    month = request.args.get('month')

    conn = sqlite3.connect('FreshFruit.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM fruits JOIN fruit_month ON fruits.id = fruit_month.fruit_id WHERE fruit_month.month_id = ?', (month,))
    results = cursor.fetchall()
    conn.close()

    fruits = []
    for row in results:
        fruit = {"id" : row[0], "name" : row[1], "image" : row[2]}
        fruits.append(fruit)

    return jsonify({'status': 'success', 'data' : {'fruits' : fruits}})


if __name__ == '__main__':
    app.run()