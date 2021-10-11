# import libraries
from flask import Flask, redirect, url_for

app = Flask(__name__)

# route the app
@app.route('/admin')
def admin():
    return 'Hello Admin, Welcome to HexNbit'

@app.route('/guest/<guest>')
def guest(guest):
    return 'Hello %s, Welcome' % guest

@app.route('/user/<name>')
def user(name):
    if name =='admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest',guest = name))

if __name__ == '__main__':
    app.run(debug = True)
