import os, sys
from flask.ext.login import UserMixin

sys.path.insert(1, '/home/vitold/bin/google_appengine')
sys.path.insert(1, '/home/vitold/bin/google_appengine/lib/yaml/lib')

from google.appengine.ext import db

class BlogPost(db.Model):
    title = db.StringProperty()
    body = db.TextProperty()
    date = db.DateTimeProperty()


# def singleton(cls):
#     instances = {}
#     def getinstance():
#         if cls not in instances:
#             instances[cls] = cls()
#         return instances[cls]
#     return getinstance
#
# @singleton
class User(UserMixin):
    # proxy for a database of user

    id = 'Vitold'
    password = 'ca6ba2c05c2117e156b6d06600dcb1e9'

