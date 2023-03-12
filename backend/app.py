from main import app
from models.fakulteti import Fakulteti
from models.user import User
from resources.user import UserListResource
@app.route('/')
def home():
    return '<h1>Hello World!</h1>'
if __name__ == '__main__':
    app.run()