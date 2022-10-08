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
    months = conn.execute('SELECT * FROM months').fetchall()
    conn.close()

    #TODO improve naming of properties in json
    return jsonify({'status': 'success', 'data' : {'months' : months}})


@app.route('/fruits', methods=['GET'])
def fruits():

    month = request.args.get('month')

    conn = sqlite3.connect('FreshFruit.db')
    fruits = conn.execute('SELECT * FROM fruits JOIN fruit_month ON fruits.id = fruit_month.fruit_id WHERE fruit_month.month_id = ?', (month,)).fetchall()
    conn.close()

    #TODO improve naming of properties in json
    return jsonify({'status': 'success', 'data' : {'fruits' : fruits}})


if __name__ == '__main__':
    app.run()