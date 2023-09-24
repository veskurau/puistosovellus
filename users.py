from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text
from db import db



def login(username, password):
    sql = text("SELECT id, password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["username"] = username
            return True
        else:
            return False

def logout():
    del session["username"]

def register(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = text("INSERT INTO users (username,password,admin) VALUES (:username,:password,:admin)")
        db.session.execute(sql, {"username":username, "password":hash_value, "admin":'0'})
        db.session.commit()
    except:
        return False
    return login(username, password)

