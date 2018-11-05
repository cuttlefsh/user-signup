from flask import Flask, request, redirect, render_template
import re

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

"""@app.route("/signup", methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    if username == "":
        error = "Please enter a username between 3 and 20 characters. No spaces allowed!"
        return redirect("/?error=" + error)
    if password == "":
        error = "Please enter a password between 3 and 20 characters. No spaces allowed!"
        return redirect("/?error=" + error)
    if verify_password != password:
        error = "Passwords do not match!"
        return redirect("/?error=" + error)
            
    
    return render_template('signup-form.html', username=username, password=password, verify_password=verify_password, email=email)
    return render_template('signup-form.html', username=request.form['username'], password=request.form['password'], verify_password=['verify_passsword'], email=request.form['verify_password'])
    """

@app.route("/", methods=['POST', 'GET'])
def index():
    username = ''
    email = ''
    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''
    title = 'Signup'

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify_password = request.form['verify_password']
        email = request.form['email']

        for i in username:
            if i.isspace():
                username_error = 'Username may not contain spaces.'
                username = ''
            else:
                if (len(username) < 3) or (len(username) > 20):
                    username_error = 'Username needs to be between 3-20 characters.'
                    username = ''

        if not username:
            username_error = 'Not a valid username'
            username = ''

        for i in password:
            if i.isspace():
                password_error = 'Password may not contain spaces.'
                password = ''
            else:
                if (len(password) < 3) or (len(password) > 20):
                    password_error = 'Password needs to be between 3 and 20 characters.'
                    password = ''
        
        if not password:
            password_error = 'Not a valid password'
            password = ''

        if password != verify_password:
            verify_password_error = 'Passwords do not match.'

        if (email != '') and (not re.match('^[a-zA-Z0-9_.+=]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email)):
            email_error = 'This is not a valid email.'
            email = ''

        if (not username_error) and (not password_error) and (not verify_password_error) and (not email_error):
            return redirect('/confirmation?username={0}'.format(username))

    return render_template('new_user_signup.html', title=title, username=username, email=email, username_error=username_error, password_error=password_error, verify_password_error=verify_password_error, email_error=email_error)

@app.route('/confirmation')
def confirmation():
    title = "You made it!"
    username = request.args.get('username')
    return render_template('confirmation.html', title=title, username=username)

if __name__ == '__main__':
    app.run()