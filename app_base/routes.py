from app_base import app, db
from flask import render_template, request, url_for, flash ,redirect
from app_base.forms import RegistrationForm, LoginForm, ContactForm
from app_base.models import User, Contact, check_password_hash

# Imports Flask-Login Module/functions
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
@login_required
def home():
    
    return render_template("main.html")
 

@app.route("/what_we_do")
@login_required   
def what_we_do():
    return render_template("what_we_do.html") 

@app.route("/who_we_are")
@login_required
def who_we_are():
    return render_template("who_we_are.html")

@app.route("/login", methods = ["GET","POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        user_email = form.email.data
        password = form.password.data
        logged_user = User.query.filter(User.email == user_email).first()
        if logged_user and check_password_hash(logged_user.password,password):
            login_user(logged_user)
            print(current_user.username)
            return redirect(url_for('home'))
    return render_template('login.html', form = form)
   # return render_template("login.html")

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login')) 

@app.route("/register", methods=["GET", "POST"])
def sign_up():
    form = RegistrationForm()
    if request.method == "POST" and form.validate():
        flash("Thanks for Signing Up!")
        # Gathering Form Data
        username = form.username.data
        email = form.email.data
        password = form.password.data
        print(username, email, password)

        # Add Form Data to User Model Class
        user = User(username, email, password)
        db.session.add(user) # Start communication with Database
        db.session.commit() # Will save data to Database
        return redirect(url_for('home'))

    else:
        flash("Your form is missing some data!")
    return render_template('register.html', form = form)
    #return render_template('register.html', title='register', form = form)

@app.route("/contact", methods =["GET","POST"])
@login_required 
def cont():
    form = ContactForm()
    if request.method == "POST" and form.validate():
        print("thats work")
        flash("Thanks for left Contact info")
        name = form.name.data
        email = form.email.data
        phone = form.phone.data
        text__message = form.text__message.data
        print(name,email,phone,text__message)

        contact__message = Contact(name, email, phone, text__message)
        db.session.add(contact__message)
        db.session.commit()
        return redirect(url_for("home"))
    else:
        flash("something went wrong")   
    return render_template("contact.html", form = form)     



