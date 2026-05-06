from app import db
from app.models import User
from werkzeug.security import generate_password_hash

def init_db(app):
    with app.app_context():
        # For the next few lines, treat this app as the active application
        '''
            Flask uses a context stack:
                When a request comes → Flask pushes context
                When request ends → Flask pops it

            app.app_context() manually pushes that context.
        '''
        db.create_all()
        create_admin()

def create_admin():
    admin = User.query.filter_by(role="admin").first()
    
    if not admin:
        admin = User(
            email="basubinayak05@gmail.com",
            password=generate_password_hash("admin05"),
            full_name="Quiz Master",
            role="admin"
        )
        db.session.add(admin)
        db.session.commit()
        print("Admin created successfully")
    else:
        print("Admin already exists")
        