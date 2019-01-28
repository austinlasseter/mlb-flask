from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def homepage():
    return render_template("main.html")

@application.route('/dashboard/')
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    application.run()
