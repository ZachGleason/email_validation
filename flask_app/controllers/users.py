from flask import render_template, request, redirect 
from flask_app.models.user import User
from flask_app import app

@app.route('/')
def index():
    return render_template("form.html")

@app.route('/process', methods=["POST"])
def main():
    if not User.validate_user(request.form):
        return redirect('/')
    User.save(request.form)
    return redirect('/results')

@app.route('/results')
def result():
    return render_template("result.html", users = User.get_all())
