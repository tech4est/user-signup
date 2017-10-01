from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/testing")
def testing():
    return render_template('testing.html')

def is_empty_string(some_chars):
    if some_chars == "":
        return True
    else:
        return False

def char_count(count):
    if len(count) < 3 or len(count) > 20:
        return True
    else:
        return False

def contains_space(any_spaces):
    if " " in any_spaces:
        return True
    else:
        return False

@app.route('/', methods=['POST'])
def validate_index():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if is_empty_string(username) or char_count(username) or contains_space(username):
        username_error = "That's not a valid username"
        username = ''

    if is_empty_string(password) or char_count(password) or contains_space(password):
        password_error = "That's not a valid password"
        password = ''

    if is_empty_string(verify) or password != verify:
        verify_error = "Passwords don't match"

    if email is "":
        email = ''
    else:
        if char_count(email) or contains_space(email):
            email_error = "Not a valid email (Must contain @, no spaces, 3-20 characters)"

    if not username_error and not password_error and not verify_error and not email_error:
        return redirect('/welcome') 
    else:                                                  
        return render_template('index.html', username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error)

@app.route('/welcome', methods=['POST'])
def welcome():
    username = request.form['username']
    return render_template('welcome.html', username=username)

app.run()