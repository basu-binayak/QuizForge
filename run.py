from app import create_app
from app.db_init import init_db

# Create the app
app = create_app()

# Initialize Db and create admin
init_db(app=app)

if __name__ == "__main__":
    app.run(debug=True)