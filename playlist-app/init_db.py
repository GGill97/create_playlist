from app import app
from models import db

# Create an application context
with app.app_context():
    # Initialize the database schema
    db.create_all()
