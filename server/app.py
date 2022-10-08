from flask import Flask, jsonify, request
import sqlite3

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/fruit', methods=['GET'])
def index():

    month = request.args.get('month')

    conn = sqlite3.connect('FreshFruit.db')
    fruits = conn.execute('SELECT name, image FROM fruits JOIN fruit_month ON fruits.id = fruit_month.fruit_id WHERE fruit_month.month_id = ?', (month,)).fetchall()
    conn.close()
    return jsonify({'status': 'success', 'data' : {'fruits' : fruits}})


if __name__ == '__main__':
    app.run()