# import library
from flask import *
app = Flask(__name__)
app.secret_key = "fe03_2nsnzf"

email = 'user@gmail.com'
password = '123'

# route the app to home page
@app.route('/')
def home():
    return render_template("home.html")

# route the app to login page
@app.route('/login')
def login():
    return render_template("login.html")

# route the app to success page
@app.route('/success',methods = ["POST"])
def success():
    if request.method == "POST":
        session['email']=request.form['email']
        if (request.form['email'] == email and request.form['pass'] == password):
            return render_template('success.html')
        else:
            return render_template('login_fail.html')

# route the app to logout page
@app.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email',None)
        return render_template('logout.html')
    else:
        return '<p>user already logged out!</p>'

# route the app to profile page
@app.route('/profile')
def profile():
    if 'email' in session:
        email = session['email']
        return render_template('profile.html',name=email)  
    else:
        return '<p>do login first</p>'

if __name__ == '__main__':
    app.run(debug = True)
