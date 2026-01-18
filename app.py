import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from flask import session, redirect, url_for, flash
from flask import Flask, render_template, request,  redirect, url_for, flash
from init_db import init_db

init_db()



app = Flask(__name__)
app.secret_key = "travelsathi_secret_key"

app.config.update(
    SESSION_COOKIE_SECURE=True,      # HTTPS only (Render)
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax"
)


from routes.planner import planner

app.register_blueprint(planner)

def get_db():
    return sqlite3.connect("travelsathi.db")
def init_trips_table():
    db = get_db()
    db.execute("""
        CREATE TABLE IF NOT EXISTS trips (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_email TEXT,
            destination TEXT,
            days INTEGER,
            people INTEGER,
            budget INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    db.commit()





@app.route("/")
def home():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    # ✅ Already logged in → don’t show login again
    if "user_id" in session:
        return redirect(url_for("home"))

    if request.method == "POST":
        email = request.form.get("email", "").lower().strip()
        password = request.form.get("password", "")

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, name, email, password FROM users WHERE email = ?",
            (email,)
        )
        user = cursor.fetchone()
        conn.close()

        # ❌ Case 1: Email does not exist
        if not user:
            flash("Account not found. Please register first.", "warning")
            return redirect(url_for("register"))

        # ❌ Case 2: Password incorrect
        if not check_password_hash(user[3], password):
            flash("Incorrect password. Please try again.", "danger")
            return redirect(url_for("login"))

        # ✅ Case 3: Login successful
        session.clear()  # 🔥 IMPORTANT
        session["user_id"] = user[0]
        session["user_name"] = user[1]
        session["user_email"] = user[2]
        session.modified = True  # 🔥 IMPORTANT

        flash("Login successful!", "success")
        return redirect(url_for("home"))

    return render_template("login.html")





@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"].strip()
        email = request.form["email"].lower().strip()
        password = request.form["password"]

        hashed_password = generate_password_hash(password)

        conn = get_db()
        cursor = conn.cursor()

        try:
            cursor.execute(
                """
                INSERT INTO users (name, email, password)
                VALUES (?, ?, ?)
                """,
                (name, email, hashed_password)
            )
            conn.commit()

            flash("Registration successful! Please login.", "success")
            return redirect(url_for("login"))

        except sqlite3.IntegrityError:
            flash("Email already exists. Please login.", "danger")

        finally:
            conn.close()   # ✅ ALWAYS closes connection

    return render_template("register.html")



@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("home"))


@app.route("/destinations")
def destinations():
    return render_template("destinations.html")

@app.route("/hotels")
def hotels():
    return render_template("hotels.html")


@app.route("/flights")
def flights():
    return render_template("travel-options.html")



@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/faqs")
def faqs():
    return render_template("faqs.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

@app.route("/terms")
def terms():
    return render_template("terms.html")


@app.route("/reset-db")
def reset_db():
    from init_db import init_db
    init_db()
    return "✅ Database reset successful"

if __name__ == "__main__":
    app.run()
