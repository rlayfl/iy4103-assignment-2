from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Routing

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

@app.route("/createproduct")
def create_product():
    return render_template("createProduct.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/loggedout")
def logged_out():
    return render_template("loggedOut.html")

@app.route("/login")
def login():
    return render_template("loggedOut.html")

@app.route("/products")
def products():

    products = Product.query.all()
    return render_template("products.html", products=products)

@app.route("/register")
def register():
    return render_template("register.html")

# Database Objects

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(500), nullable=True)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

# CRUD Methods

@app.route("/submit_product", methods=["POST"])
def submit_product():
    name = request.form.get("productName")
    price = request.form.get("price")
    description = request.form.get("description")

    new_product = Product(name=name, price=price, description=description)
    db.session.add(new_product)
    db.session.commit()

    return redirect(url_for('products'))

if __name__ == '__main__':
    app.run(debug = True)