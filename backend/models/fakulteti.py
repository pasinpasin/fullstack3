from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from main import db
class Fakulteti(db.Model):
  id = db.Column(db.Integer(), primary_key=True)
  emertimi = db.Column(db.String(255), nullable=False)
 
  created_at = db.Column(db.DateTime, default=datetime.now)
  updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

  def __init__(self, emertimi):
    self.emertimi = emertimi
  def __repr__(self):
    return "<Fakulteti '{}'>".format(self.emertimi)
  