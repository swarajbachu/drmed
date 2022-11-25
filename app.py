from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import git 
import os
import socket

socket.gethostbyname("ims-mysql-server.mysql.database.azure.com")
app = Flask(__name__)

host = 'ims-mysql-server.mysql.database.azure.com'
username = 'swarajbachu@ims-mysql-server'
password = 'Google@class'
dataBase = 'test'


app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{host}:{password}@{username}:3306/{dataBase}'
# sql lite database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/hospital.db'

db = SQLAlchemy(app)



@app.route('/git_update', methods=['POST'])
def git_update():
    repo = git.Repo('./drmed')
    origin = repo.remotes.origin
    repo.create_head('main',
                     origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return '', 200

@app.route('/')
def hello_world():
   # return 'Hello, World!'
    return render_template('index.html')

# @app.route('/post_patient_records', methods=['POST'])
# def post_patient_records():

@app.route('/amstrong_number/<int:num>')
def amstrong_number(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        return jsonify({"result": "Amstrong Number"})
    else:
        return jsonify({"result": "Not Amstrong Number"})

if __name__ == '__main__':
    app.run(debug=True)
