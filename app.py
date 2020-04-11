import os
from flask import Flask, render_template, redirect, request, url_for, flash
from forms import RegistrationForm, LoginForm
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['SECRET_KEY'] = 'c37adb1952ee82a1f6ecc2cd1bf10742'
app.config["MONGO_DBNAME"] = 'cocktails'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-9apc7.mongodb.net/cocktails?retryWrites=true&w=majority'

mongo = PyMongo(app)



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', recipes=mongo.db.recipes.find())

#@app.route('/drinks')
#def home():
#    return render_template('drinks.html', title='Drinks')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', '_success_')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@drinks.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password!', 'danger')
    return render_template('login.html', title='Log In', form=form)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)