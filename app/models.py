from datetime import datetime, timezone
from app import db

# ------------------ USER ------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(120), nullable=False)
    qualification = db.Column(db.String(120))
    dob = db.Column(db.Date)
    role = db.Column(db.String(20), nullable=False)  # admin / user
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    
    # create a relationship with Score
    scores = db.relationship("Score", backref="user", lazy=True)

# ------------------ SUBJECT ------------------
class Subject(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)

    chapters = db.relationship("Chapter", backref="subject", cascade="all, delete", lazy=True)


# ------------------ CHAPTER ------------------
class Chapter(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey("subject.id"), nullable=False)

    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)

    quizzes = db.relationship("Quiz", backref="chapter", cascade="all, delete", lazy=True)


# The db.relationship is the Python-side abstraction, meaning you can do subject.chapters to get all chapters of a subject, while the backref="subject" automatically creates the reverse access—so from a Chapter object, you can directly do chapter.subject without defining it explicitly. 
# The cascade="all, delete" ensures that if a Subject is deleted, all its associated Chapters are also deleted automatically (maintaining referential integrity). 
# The lazy=True means the related Chapters are loaded only when accessed (lazy loading), not when the Subject is first queried, which improves performance. 
# The same pattern repeats between Chapter and Quiz, creating a clean, navigable object graph where you can move both forward (Subject → Chapters → Quizzes) and backward (Quiz → Chapter → Subject) using simple Python attributes instead of writing joins manually.


# ------------------ QUIZ ------------------
class Quiz(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    chapter_id = db.Column(db.Integer, db.ForeignKey("chapter.id"), nullable=False)

    date_of_quiz = db.Column(db.DateTime)
    duration = db.Column(db.String(10))  # HH:MM format
    remarks = db.Column(db.Text)

    questions = db.relationship("Question", backref="quiz", cascade="all, delete", lazy=True)
    scores = db.relationship("Score", backref="quiz", lazy=True)


# ------------------ QUESTION ------------------
class Question(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey("quiz.id"), nullable=False)

    question_statement = db.Column(db.Text, nullable=False)

    option1 = db.Column(db.String(255), nullable=False)
    option2 = db.Column(db.String(255), nullable=False)
    option3 = db.Column(db.String(255), nullable=False)
    option4 = db.Column(db.String(255), nullable=False)

    correct_option = db.Column(db.Integer, nullable=False)  # 1,2,3,4


# ------------------ SCORE ------------------
class Score(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    quiz_id = db.Column(db.Integer, db.ForeignKey("quiz.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    time_stamp = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    total_score = db.Column(db.Integer)
    
    # Add unique constraint to prevent duplicate attempts:
    __table_args__ = (
        db.UniqueConstraint('quiz_id', 'user_id', name='unique_attempt'),
    )