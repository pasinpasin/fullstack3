import psycopg2
class Config(object):
    pass
class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG = True
    DB_CONN = psycopg2.connect(
        host="balarama.db.elephantsql.com",
        database="rnuyqlvw ",
        user='rnuyqlvw',
        password='nHklXes_itjcTzl-zpDNHdBkt_r2vk6Q',
       
        )
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://postgres://rnuyqlvw:nHklXes_itjcTzl-zpDNHdBkt_r2vk6Q@balarama.db.elephantsql.com/rnuyqlvw'
    #SQLALCHEMY_DATABASE_URI='postgres://rnuyqlvw:nHklXes_itjcTzl-zpDNHdBkt_r2vk6Q@balarama.db.elephantsql.com/rnuyqlvw'
    SQLALCHEMY_ECHO = True
