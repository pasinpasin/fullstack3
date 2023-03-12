import psycopg2
class Config(object):
    pass
class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG = True
    """ DB_CONN = psycopg2.connect(
        host="balarama.db.elephantsql.com",
        database="rnuyqlvw ",
        user='rnuyqlvw',
        password='nHklXes_itjcTzl-zpDNHdBkt_r2vk6Q',
       
        ) """
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://rnuyqlvw:nHklXes_itjcTzl-zpDNHdBkt_r2vk6Q@balarama.db.elephantsql.com/rnuyqlvw'
    #SQLALCHEMY_DATABASE_URI='postgres://gentiani:8vlbwUgUU7JFsG0QUFNsZ7vH5GiXARzS@dpg-cg5o8e64daddn4p834qg-a.frankfurt-postgres.render.com/testdb_7h9r'
    SQLALCHEMY_ECHO = True
    #CONNSTR = f'postgresql://gjyli.gentian:iowg09NfYATH@mydb.ep-floral-cake-977997.eu-central-1.aws.neon.tech/neondb'
