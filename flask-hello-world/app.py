from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
@app.route("/test")
def search():
    return "Hello"

def hello_world():
    return "Hello, World!"

if __name__== '__main__':
    app.run()