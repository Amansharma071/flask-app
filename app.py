from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/about") 
def about():
    return "This is about page"

@app.route("/users")
def users():
    return "This is the users page"

@app.route("/user/<name>")
def user(name):
    return f"Hello, {name}"

@app.route("/student/<name>/")
def student(name, course):
    return f"Hello, {name}. You are enrolled in {course} course."

if __name__ == "__main__":
    app.run(debug=True)
