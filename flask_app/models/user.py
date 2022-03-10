from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class User:
    def __init__(self,data):
        self.id = data["id"]
        self.email = data["email"]
        self.created_at = data["created_at"]

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (email) VALUES (%(email)s);"
        return connectToMySQL('email_valid').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('email_valid').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

    @staticmethod
    def validate_user(email):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('email_valid').query_db(query, email)
        print(results)
        if len(results) >= 1:
            flash("Email address is already taken.")
            is_valid=False
        if not EMAIL_REGEX.match(email['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid
