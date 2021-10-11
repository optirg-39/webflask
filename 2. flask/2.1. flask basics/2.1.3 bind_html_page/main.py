# import libraries
from flask import Flask
from flask import render_template

#creating the Flask class object 
app = Flask(__name__)

#route the app
@app.route('/')
def home():
    return render_template("index.html")

if __name__ =='__main__':
    app.run(debug = True, port=5000)
