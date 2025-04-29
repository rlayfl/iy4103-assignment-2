from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def index():
    return render_template("about.html")

@app.route("/basket")
def index():
    return render_template("basket.html")

@app.route("/checkout")
def index():
    return render_template("checkout.html")

@app.route("/faq")
def index():
    return render_template("faq.html")

@app.route("/loggedOut")
def index():
    return render_template("loggedOut.html")

@app.route("/login")
def index():
    return render_template("loggedOut.html")

@app.route("/register")
def index():
    return render_template("register.html")

if __name__ == '__main__':
    app.run(debug = True)