from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="test_management"
)
cur = db.cursor(dictionary=True)

if db.is_connected():
    print("✅ Connected to MySQL (XAMPP)")

@app.route('/add-test', methods=['POST'])
def add():
    d = request.json
    cur.execute("INSERT INTO tests (name, price, details) VALUES (%s, %s, %s)",
                (d['name'], d['price'], d['details']))
    db.commit()
    return jsonify(msg="Test added")

@app.route('/get-tests')
def get():
    cur.execute("SELECT * FROM tests")
    return jsonify(cur.fetchall())

@app.route('/edit-test/<int:id>', methods=['PUT'])
def edit(id):
    d = request.json
    cur.execute("UPDATE tests SET name=%s, price=%s, details=%s WHERE id=%s",
                (d['name'], d['price'], d['details'], id))
    db.commit()
    return jsonify(msg="Test updated")

@app.route('/delete-test/<int:id>', methods=['DELETE'])
def delete(id):
    cur.execute("DELETE FROM tests WHERE id=%s", (id,))
    db.commit()
    return jsonify(msg="Test deleted")

if __name__ == '__main__':
    app.run(debug=True)
