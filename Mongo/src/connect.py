from mongoengine import connect
import configparser

config = configparser.ConfigParser()
config.read('src/config.ini')  # to read the config file

m_user = config.get('DB', 'user')
m_pass = config.get('DB', 'pass')
db_name = config.get('DB', 'db_name')
domain = config.get('DB', 'domain')


connect(host = f"mongodb+srv://{m_user}:{m_pass}@{domain}/{db_name}?retryWrites=true&w=majority")
