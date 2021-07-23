import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

from dotenv import load_dotenv
load_dotenv()

database_path = os.getenv("DATABASE_URL")
# database_path = 'postgresql://postgres:doublea@localhost:5432/testcap'
# database_path = 'postgres://rreakxlnuymdsk:172a4e1da231026e08fb09d4c80f3231b7e6b08cbbd3b1dfd8844421fbf98ec6@ec2-52-23-40-80.compute-1.amazonaws.com:5432/d93bv217jfk5vh'
# database_path = 'postgres://wlqgounsvufolj:742ba2fb146391690bad46cddd272a6e597b6e8702b67a04cbd62fb164508da6@ec2-52-23-40-80.compute-1.amazonaws.com:5432/d9v89l5k5pmonn'

db = SQLAlchemy()

print(database_path)

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
Person
Have title and release year
'''
class Person(db.Model):  
  __tablename__ = 'People1'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  catchphrase = Column(String)

  def __init__(self, name, catchphrase=""):
    self.name = name
    self.catchphrase = catchphrase

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'catchphrase': self.catchphrase}