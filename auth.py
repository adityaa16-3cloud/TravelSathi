from functools import wraps
from flask import session, redirect, url_for, flash

def login_required(route_function):
    @wraps(route_function)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            flash("Please login to access this page.", "warning")
            return redirect(url_for("login"))
        return route_function(*args, **kwargs)
    return wrapper