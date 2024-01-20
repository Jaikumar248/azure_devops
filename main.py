from flask import Flask


app = Flask(__name__)
@app.route('/')
def hello():
    print("Hello jaikumar")
    return "I am JAIKUMAR"

if __name__ == "__main__":
    app.run()
