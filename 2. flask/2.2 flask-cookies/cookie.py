# import libraries
from flask import request, make_response

#creating the Flask class object
app = Flask(__name__)

@app.route("/cookies")
def cookies():
    res = make_response("Cookies", 200)
    
    # to set the cookies
    res.set_cookie("mode", "dark")
    
    # to get the cookies
    temp_cookies = request.cookies
    print(temp_cookies)
    
    return res

if __name__ =='__main__':
    app.run(debug = True, port=5000)
