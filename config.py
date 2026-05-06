# import the os module 
import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# __file__ → refers to the current Python file.
# os.path.dirname(__file__) → gives the folder containing this file.
# os.path.abspath(...) → converts that into a full absolute path. 
# Here, we get d:\\GITHUB_RESUME\\QuizForge

class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR,"quizforge.db")
    # SQLite is different since it does not use a server. I directly works on the file of our system.
    # Database URIs follow the structure - dialect://username:password@host:port/database
    # The third / in sqlite:/// - This is a local file path, not a network location
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # By defult, SQLALCHEMY manages every object(row) you load from the database 
    # It detects changes like - user.name = Binayak" and emits signals whenever something changes 
    # This creates a extra overhead ( memory + CPU ) - most apps don't need that. Hence turning it off is a way to reduce the significant overhead 
    
    SECRET_KEY = "bbinayak05"