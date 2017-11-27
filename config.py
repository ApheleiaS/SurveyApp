# DB Config 
import os
basedir = os.path.abspath(os.path.dirname(__file__))

# This is the path of our database file.
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db') 

# The folder where we will store the SQLAlchemy-migrate data files.
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository') 

# This is for WTForms
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'