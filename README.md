# 🚀 QuizForge

**QuizForge** is a modular, multi-user quiz platform built using **Flask**, **Jinja2**, and **SQLite**. It is designed as an exam preparation system where an administrator (Quiz Master) can create and manage quizzes, while users can attempt them and track their performance.

---

## 📌 Features

### 👨‍🏫 Admin (Quiz Master)

* Pre-configured admin (no registration required)
* Create, edit, and delete **Subjects**
* Organize **Chapters** under subjects
* Create and manage **Quizzes**
* Add/edit/delete **MCQ questions** (single correct option)
* Set quiz duration and schedule
* Search users, subjects, and quizzes
* View summary dashboards and analytics

---

### 👨‍🎓 User

* Register and login securely
* Browse subjects and chapters
* Attempt quizzes of interest
* View quiz history and scores
* Track performance over time
* (Optional) Timed quiz experience

---

## 🧱 Tech Stack

| Layer    | Technology                   |
| -------- | ---------------------------- |
| Backend  | Flask                        |
| Frontend | HTML, CSS, Bootstrap, Jinja2 |
| Database | SQLite                       |
| Optional | Chart.js (for analytics)     |

---

## 🗂️ Project Structure

```
QuizForge/
│
├── app/
│   ├── __init__.py
│   ├── models/
│   ├── routes/
│   ├── templates/
│   ├── static/
│   └── utils/
│
├── instance/
│   └── database.db
│
├── migrations/ (optional)
├── requirements.txt
├── config.py
└── run.py
```

---

## 🧩 Database Design

### 🔹 User

* id (PK)
* email (username)
* password
* full_name
* qualification
* dob

### 🔹 Admin

* Pre-created in DB (no registration)

### 🔹 Subject

* id (PK)
* name
* description

### 🔹 Chapter

* id (PK)
* subject_id (FK)
* name
* description

### 🔹 Quiz

* id (PK)
* chapter_id (FK)
* date_of_quiz
* duration
* remarks

### 🔹 Question

* id (PK)
* quiz_id (FK)
* question_statement
* options (MCQ)
* correct_option

### 🔹 Score

* id (PK)
* quiz_id (FK)
* user_id (FK)
* timestamp
* total_score

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/basu-binayak/QuizForge.git
cd QuizForge
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
python run.py
```

---

## 🔐 Default Admin Credentials

```
Email: admin@quizforge.com
Password: admin123
```

> ⚠️ Ensure admin is created programmatically when DB initializes.

---

## 📊 Core Functionalities

* Full **CRUD operations** for Subjects, Chapters, Quizzes
* MCQ-based quiz system (single correct answer)
* Score tracking and history
* Clean dashboard interfaces
* Programmatic database creation (no manual DB setup)

---

## 🌐 API Support (Optional)

* REST APIs for:

  * Subjects
  * Chapters
  * Quizzes
* JSON responses via Flask routes or Flask-RESTful

---

## 🎨 Enhancements (Optional)

* Responsive UI with Bootstrap
* Chart-based analytics (Chart.js)
* Flask-Login for authentication
* Form validation (frontend + backend)

---

## 🧠 Learning Objectives

This project helps in understanding:

* Flask application structuring (Blueprints)
* MVC-like architecture
* Relational database design (SQLite)
* User authentication basics
* CRUD operations
* Template rendering with Jinja2

---

## 🚧 Future Improvements

* Role-based authentication system
* Timer-based quiz enforcement
* Leaderboards
* Pagination and filtering
* Deployment (Render / Vercel / Docker)

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.

---

## 📜 License

This project is for educational purposes.

---

