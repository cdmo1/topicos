from tumbrl import app, database
from models import User, Posts

with app.app_context():
    database.create_all()
