from flask import Flask

application = Flask(__name__)
@application.route('/')
def index():
    # use html syntax inside return
    return '<html><body><h1>Welcome to HexNbit</h1></body></html>'

if __name__ == '__main__':
    application.run(debug = True)
