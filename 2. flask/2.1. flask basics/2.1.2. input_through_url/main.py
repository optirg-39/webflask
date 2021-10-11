# import library
from flask import Flask  

#creating the Flask class object 
app = Flask(__name__)

#route the app
@app.route('/')
def home():  
    return "Home Page"; 
@app.route('/admin')
def hexnbit_admin():
    return "Hi, You are the Admin of hexnbit"
@app.route('/guest/<guest>')
def hexnbit_guest(guest):
    return "Hi {}, Welcome to Hexnbit".format(guest)

if __name__ =='__main__':
    app.run(debug = True, port=5000) 
