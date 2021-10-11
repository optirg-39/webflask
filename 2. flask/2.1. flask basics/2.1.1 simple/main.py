# import library
from flask import Flask  

#creating the Flask class object 
app = Flask(__name__)

#route the app
@app.route('/')
def home():
    return "Home Page";

@app.route('/welcome')
def welcome():
    return "Welcome to  Hexnbit"

if __name__ =='__main__':
    app.run(debug = True, port=5000)
