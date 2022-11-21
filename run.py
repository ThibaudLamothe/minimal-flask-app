from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/hello/<username>")
def hello_name(username):
    return f"Hello {username}!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
