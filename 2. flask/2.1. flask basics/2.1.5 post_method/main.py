from flask import *
app = Flask(__name__)

# admin credentials
admin_username = "admin"
admin_password = "123"

@app.route('/login', methods=['POST'])
def login():
  uname = request.form['username']
  passwrd = request.form['password']
  if uname == admin_username and passwrd == admin_password:
    return "Welcome to the admin panel"
  else:
    return "Password or Username Incorrect"

if __name__ == '__main__':
  app.run(debug=True)
