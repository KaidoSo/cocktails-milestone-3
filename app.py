import os
from flask import Flask, render_template, redirect, request, url_for, flash, session
from forms import RegistrationForm, LoginForm
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt

app = Flask(__name__)

app.config['SECRET_KEY'] = 'c37adb1952ee82a1f6ecc2cd1bf10742'
app.config["MONGO_DBNAME"] = 'cocktails'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-9apc7.mongodb.net/cocktails?retryWrites=true&w=majority'

mongo = PyMongo(app)



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', recipes=mongo.db.recipes.find())



@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert_one({'name': request.form['username'],
                            'password': hashpass,
                            'email': request.form['email']})
            session['username'] = request.form['username']
            flash(f'Account created for {form.username.data}!', 'success')
            return redirect(url_for('home'))
        flash('This username is taken. Please choose a different one.', 'danger')        
        return redirect(url_for('register'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'logged_in' in session:
        if session['logged_in'] == True:
            return redirect(url_for('home', title="Log In"))

    form = LoginForm()

    if form.validate_on_submit():
        print("Hello")
        users = mongo.db.users
        db_user = users.find_one({'name': request.form['username']})
        print(db_user)
        
        if db_user:
            if bcrypt.hashpw(request.form['password'].encode('utf-8'),
                            db_user['password']) == db_user['password']:
                session['username'] = request.form['username']
                session['logged_in'] = True
                flash(f'Welcome, {form.username.data}!', 'success')
                return redirect(url_for('home', title="Log In", form=form))
        flash('Login Unsuccessful. Please check username and password!', 'danger')
    return render_template('login.html', title='Log In', form=form)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    recipe_db = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template('drink.html', recipe=recipe_db)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)