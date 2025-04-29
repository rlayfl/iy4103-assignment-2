from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/basket")
def basket():
    return render_template("basket.html")

@app.route("/checkout")
def checkout():
    return render_template("checkout.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/loggedout")
def logged_out():
    return render_template("loggedOut.html")

@app.route("/login")
def login():
    return render_template("loggedOut.html")

@app.route("/register")
def register():
    return render_template("register.html")

if __name__ == '__main__':
    app.run(debug = True)