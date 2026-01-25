from flask import Flask, render_template, request, redirect
import mysql.connector
import hashlib

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pankaj@3437",
    database="auth_system"
)

cursor = db.cursor()

@app.route("/index")
def home():
    return render_template("index.html")

@app.route("/login")
def signup_page():
    return render_template("login.html")

@app.route("/signup")
def signup_page():
    return render_template("signup.html")

@app.route("/signup", methods=["POST"])
def signup():
    username = request.form["username"]
    email = request.form["email"]
    password = hashlib.sha256(request.form["password"].encode()).hexdigest()

    try:
        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
            (username, email, password)
        )
        db.commit()
        return "Signup successful"
    except:
        return "Email already exists"

@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = hashlib.sha256(request.form["password"].encode()).hexdigest()

    cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
    user = cursor.fetchone()

    if user:
        return f"Welcome {user[1]}"
    else:
        return "Invalid Creadential"

if __name__ == "__main__":
    app.run(debug=True)
