from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from flask"

@app.route("/<name>")
def user(name):
    return f"Hello from {name}"

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="super admin"))

if __name__ == "__main__":
    app.run()
