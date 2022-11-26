from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import git 
import os
from sqlalchemy import create_engine,text
# from flask_mysqldb import MySQL


host = 'ap-south.connect.psdb.cloud'
username = 'df7zqjydykpesxl5oy7p'
password = 'pscale_pw_Vj3nfrYHeCMt8AhC1yH8u0sL6Ldvca6w2eUQhz2DrKJ'
dataBase = 'mrmed'

host2 = 'https://ims-mysql-server.mysql.database.azure.com'
username2 = 'swarajbachu@ims-mysql-server'
password2 = 'Google@class'
dataBase2 = 'test'


app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username2}:{password2}@{host2}:3306/{dataBase2}'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/hospital.db'


uri = f'mysql+pymysql://{username2}:{password2}@{host2}:3306/{dataBase2}'

#db = SQLAlchemy(app)


# app.config['MYSQL_HOST'] = host
# app.config['MYSQL_USER'] = username
# app.config['MYSQL_PASSWORD'] = password
# app.config['MYSQL_DB'] = dataBase



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

@app.route('/patient_record', methods=['GET','POST'])
def patient_record():
    if request.method == 'POST':
        record_details = request.form
        ECG = record_details['ECG']
        #BMR = record_details['BMR']
        PE = record_details['Physical Examination']
        desease = record_details['disease']
        treatment = record_details['Treatment']
        Pid = record_details['Insurance Status']
        # Year_of_diagnosis = record_details['Year_of_diagnosis']
        Insurence_id = record_details['Doctor Name']
        hospital_name = record_details['Hospital Name']
        # print(ECG,PE,desease,Pid,Insurence_id,hospital_name)
        engine = create_engine(uri)
        with engine.connect() as conn:
            conn.execute(text("INSERT INTO patient_record_ (Pid, ECG, BMR,Year_of_diagnosis, History_of_disease,Insurance_id) VALUES (:Pid,:ECG, :BMR, :desease,:Year_of_diagnosis :Insurance_id)"), ECG=ECG, BMR=PE, desease=desease,Year_of_diagnosis=hospital_name, Insurance_id=Insurance_id,Pid=pid)
    return render_template('Treatment.html')
    
# @app.route('/amstrong_number/<int:num>')
# def amstrong_number(num):
#     sum = 0
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** 3
#         temp //= 10
#     if num == sum:
#         return jsonify({"result": "Amstrong Number"})
#     else:
#         return jsonify({"result": "Not Amstrong Number"})

if __name__ == '__main__':
    app.run(debug=True)
