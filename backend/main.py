from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig
app = Flask(__name__)
app.config.from_object(DevConfig)
#cur = app.config['DB_CONN'].cursor()
db = SQLAlchemy(app)
from models import User
@app.route('/')
def home():
    return '<h1>Hello World!</h1>'
if __name__ == '__main__':
    app.run()