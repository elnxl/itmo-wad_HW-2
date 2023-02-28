from flask import Flask, render_template, abort, request
from pymongo import MongoClient

app = Flask(__name__)

def get_db():
    client = MongoClient(host='wad_mongodb',
                         port=27017,
                         username='root',
                         password='pass')
    db = client["wad_db"]
    return db

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile', methods=['POST'])
def login():
    db = get_db()
    uname = request.form.get('uname')
    passwd = request.form.get('psw')

    user = db.wad_tb.find_one({"username": uname, "password": passwd})

    if user:
        return render_template('profile.html', name= uname)
    else:
        return abort(403)

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)