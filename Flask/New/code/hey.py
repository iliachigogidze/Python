from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    request.authorization.username
    request.authorization.password
    return '<h1>This is the index!</h1>'

if __name__=='__main__':
    app.run(debug=True)