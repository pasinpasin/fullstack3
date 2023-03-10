
from main import db
class User(db.Model):
  id = db.Column(db.Integer(), primary_key=True)
  password = db.Column(db.String(255), nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  def __init__(self, email):
    self.email = email
  def __repr__(self):
    return "<User '{}'>".format(self.email)