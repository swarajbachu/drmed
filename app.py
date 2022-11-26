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

host1 = 'sql6.freesqldatabase.com'
username1 = 'sql6580826'
password1 = 'yBDLIINgZ8'
dataBase1 = 'sql6580826'

host2 = 'https://ims-mysql-server.mysql.database.azure.com'
username2 = 'swarajbachu@ims-mysql-server'
password2 = 'Google@class'
dataBase2 = 'test'


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username1}:{password1}@{host1}:3306/{dataBase1}'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/hospital.db'


uri = f'mysql+pymysql://{username1}:{password1}@{host1}:3306/{dataBase1}'

db = SQLAlchemy(app)


# app.config['MYSQL_HOST'] = host
# app.config['MYSQL_USER'] = username
# app.config['MYSQL_PASSWORD'] = password
# app.config['MYSQL_DB'] = dataBase

def countRecords():
    engine = create_engine(uri)
    with engine.connect() as conn:
        count = conn.execute(text("SELECT COUNT(*) FROM MedicalRecord")).scalar()
        return count

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

@app.route('/patient_record/<int:pid>', methods=['GET','POST'])
def patient_record(pid):
    if request.method == 'POST':
        record_details = request.form
        ECG = record_details['ECG']
       # BMR = record_details['BMR']
        PE = record_details['Physical Examination']
        disease = record_details['disease']
        treatment = record_details['Treatment']
        Insurence_status = record_details['Insurance Status']
        Date = record_details['Year_of_diagnosis']
        doctorName = record_details['Doctor Name']
        hospital_name = record_details['Hospital Name']
        rid = countRecords()+1
        # print(ECG,PE,desease,Pid,Insurence_id,hospital_name)
        engine = create_engine(uri)
        with engine.connect() as conn:
            conn.execute(text("INSERT INTO MedicalRecord (Rid,Pid,BMR, ECG, disease,date,treatment,hospitalName,doctorName) VALUES (:Rid,:Pid,:ECG, :BMR,:Date, :disease,:treatment,:hospitalName,:doctorName)"),
                         ECG=ECG, BMR=Insurence_status, Date=Date, disease=disease, Pid=pid, Rid=rid, treatment=treatment, hospitalName=hospital_name, doctorName=doctorName)
    return render_template('Treatment.html')


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        login_details = request.form
        username = login_details['username']
        password = login_details['password']
        print(username,password)
        engine = create_engine(uri)
        with engine.connect() as conn:
            conn.execute(text("INSERT INTO doctorLogin (username, password) VALUES (:username,:password)"), username=username, password=password)
        
    return render_template('Login.html')



@app.route('/patient_details/<int:pid>', methods=['GET'])
def patient_details(pid):
    engine = create_engine(uri)
    with engine.connect() as conn:
        patient = conn.execute(text("SELECT * FROM PatientDetails WHERE Pid = :pid"), pid=pid).fetchall()
        result = conn.execute(text("SELECT * FROM MedicalRecord WHERE Pid=:pid"), pid=pid).fetchall()
        record = []
        for row in result:
            d = dict(row)
            record.append(d)
        patientDetails = dict(patient[0])
        # results = [list(row) for row in result]
        return jsonify(patientDetails,record)

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
