
from main import db
from datetime import datetime
class User(db.Model):
  id = db.Column(db.Integer(), primary_key=True)
  password = db.Column(db.String(255), nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.now)
  updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
  is_active=db.Column(db.Boolean, default=False)
  def __init__(self, email,password):
    self.email = email
    self.password=password
  def __repr__(self):
    return "<User '{}'>".format(self.email)