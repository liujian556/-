
class Set_error():
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def Database_URI(DATABASE):
    type = DATABASE.get('Type')
    engine = DATABASE.get('Engine')
    user = DATABASE.get('User')
    password = DATABASE.get('Password')
    host = DATABASE.get('Host')
    port = DATABASE.get('Port')
    database = DATABASE.get('Database')

    return '{}+{}://{}:{}@{}:{}/{}'.format(type,engine,user,password,host,port,database)

class Database_set(Set_error):
    DATABASE = {
        'Type':'mysql',
        'Engine':'pymysql',
        'User':'root',
        'Password':'123456',
        'Host':'47.113.108.244',
        'Port':'3306',
        'Database':'flask_jie'
    }

    SQLALCHEMY_DATABASE_URI = Database_URI(DATABASE)


ENV_DATABASE = {
    'database':Database_set
}

CMS_USER_ID = 'whisherocity'
