#import libraries
from flask import *
app = Flask(__name__)

# credentials
user_name = 'admin'
password = '123'

@app.route('/')
def home ():
    return render_template("home.html")

@app.route('/login')
def login():
    return render_template("login.html");

@app.route('/check', methods = ["POST"])
def check():
    if request.method == 'POST' and request.form['password'] == password and request.form['username'] == user_name:
        return redirect(url_for("success"))
    else:
        abort(401)

@app.route('/success')
def success():
    return "Successfully Login"

if __name__ == '__main__':
    app.run(debug = True)
