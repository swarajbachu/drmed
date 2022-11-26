from sqlalchemy import create_engine
import urllib

host = 'ims-mysql-server.mysql.database.azure.com'
username = 'swarajbachu@ims-mysql-server'
password = 'Google@class'
dataBase = 'test'
driver = 'mysql+pymysql'


params = urllib.parse.quote_plus(
    'Driver=%s;' % driver +
    'Server=tcp:%s,1433;' % host +
    'Database=%s;' % dataBase +
    'Uid=%s;' % username +
    'Pwd={%s};' % password +
    'Encrypt=yes;' +
    'TrustServerCertificate=no;' +
    'Connection Timeout=30;')

conn_str = 'mssql+pyodbc:///?odbc_connect=' + params
engine_azure = create_engine(conn_str)

print('connection is ok')
print(engine_azure.table_names())

