from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/signup", methods=['POST'])
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

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('base.html', error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()    