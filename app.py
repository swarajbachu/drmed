from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import git
import os
app = Flask(__name__)

host = 'ims-mysql-server.mysql.database.azure.com'
username = 'swarajbachu@ims-mysql-server'
password = 'Google@class'
dataBase = 'hospitalHistory'

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


if __name__ == '__main__':
    app.run(debug=True)
