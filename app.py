from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, DevSecOps! ss'

if __name__ == '__main__':
    app.run(debug=True)


