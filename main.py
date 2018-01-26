from flask import Flask, request, redirect, render_template
import os
import cgi
import re


app = Flask(__name__)
app.config['DEBUG'] = True

def is_valid(input):
    if ' ' in input:
        return False
    return  3 <= len(input) <= 20

def isValidEmail(email):
    if len(email) > 7:
        match = "re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)"
        if match:
            return True
        else:
            return False

                    
   


@app.route("/")
def index():
    
    return render_template('user-form.html')

@app.route("/validate-form", methods=['POST'])
def validate_form():

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify']
    email = request.form['email']

    username_error= ''
    password_error= ''
    verify_error= ''
    email_error = ''


    if not is_valid(username):
        username_error = 'not a valid username'
        username = ''


    if not is_valid(password):
        password_error= 'not a valid password'
        password = ''
    
    else:
        if not password == verify_password:
            password_error= 'password does not match'
            password = ''

    if isValidEmail(email):
        pass
    else:
        email_error = 'not valid email'

            
    
    if not username_error and not password_error and not email_error:
     
        return redirect('/valid-form?form={0}'.format(username))
    else:
        return render_template('user-form.html', username_error=username_error,
            password_error=password_error,
            username=username,
            email_error=email_error,
            email=email)
    

@app.route('/valid-form')
def valid_form():
    form = request.args.get('form')
    return '<h1>Welcome,{0}'.format(form) 




app.run()

