import os
from flask import Flask, render_template, redirect, request, url_for, flash, session
from forms import RegistrationForm, LoginForm, CreateForm, EditForm, DeleteForm
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET')
app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', recipes=mongo.db.recipes.find())


@app.route('/register', methods=['GET', 'POST'])
def register():
    # Handles registration of new users
    form = RegistrationForm()
    if form.validate_on_submit():
        # get all the users
        users = mongo.db.users
        # check if username already exists
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            # if username is new encrypt the password
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            # insert the user to DB
            users.insert_one({'name': request.form['username'],
                            'password': hashpass,
                            'email': request.form['email']})
            session['username'] = request.form['username']
            flash(f'Account created for {form.username.data}!', 'success')
            return redirect(url_for('home'))
        # duplicate username gets flash message and redirected to register page again
        flash('This username is taken. Please choose a different one.', 'danger')        
        return redirect(url_for('register'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # Login handler
    if 'logged_in' in session:
        if session['logged_in'] == True:
            return redirect(url_for('home', title="Log In"))

    form = LoginForm()

    if form.validate_on_submit():
        # get all users
        users = mongo.db.users
        # try to get the one with the same name as entered
        db_user = users.find_one({'name': request.form['username']})
        print(db_user)
        
        if db_user:
            # check password using hashing
            if bcrypt.hashpw(request.form['password'].encode('utf-8'),
                            db_user['password']) == db_user['password']:
                session['username'] = request.form['username']
                session['logged_in'] = True
                # if successful redirect to home page with Welcome message
                flash(f'Welcome, {form.username.data}!', 'success')
                return redirect(url_for('home', title="Log In", form=form))
        # if failed, redirecto to login page with error message     
        flash('Login Unsuccessful. Please check username and password!', 'danger')
    return render_template('login.html', title='Log In', form=form)


@app.route('/logout')
def logout():
    # clears the session and redirects to home page
    session.clear()
    return redirect(url_for('home'))


@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    # displays full drink recipe
    recipe_db = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template('drink.html', recipe=recipe_db)


@app.route('/create', methods=['GET', 'POST'])
def create():
    # creates a drink recipe and enters into recipes collection
    form = CreateForm(request.form)
    if form.validate_on_submit():
        # set the collection
        recipes_db = mongo.db.recipes
        # insert the new recipe
        recipes_db.insert_one({
            'name': request.form['name'],
            'user': session['username'],
            'image': request.form['image'],
            'ingredients': request.form['ingredients'],
            'instructions': request.form['instructions']
        })
        return redirect(url_for('home', title='New Drink Created'))
    return render_template('create.html', title='Create a Drink', form=form)


@app.route('/edit/<recipe_id>', methods=['GET', 'POST'])
def edit(recipe_id):
    # allows logged in user to edit a recipe they've created
    recipe_db = mongo.db.recipes.find_one_or_404({'_id': ObjectId(recipe_id)})
    if request.method == 'GET':
        form = EditForm(data=recipe_db)
        return render_template('edit.html', recipe=recipe_db, form=form)
    form = EditForm(request.form)
    if form.validate_on_submit():
        recipes_db = mongo.db.recipes
        recipes_db.update_one({
            '_id': ObjectId(recipe_id),
        }, {
            '$set': {
            'name': request.form['name'],
            'user': session['username'],
            'image': request.form['image'],
            'ingredients': request.form['ingredients'],
            'instructions': request.form['instructions'],
            }
        })
        return redirect(url_for('home', title='Drink Edited'))
    return render_template('edit.html', recipe=recipe_db, form=form)


@app.route('/delete/<recipe_id>', methods=['GET', 'POST'])
def delete(recipe_id):
    # allows logged in user to delete a recipe that they've created
    recipe_db = mongo.db.recipes.find_one_or_404({'_id': ObjectId(recipe_id)})
    if request.method == 'GET':
        form = DeleteForm(data=recipe_db)
        return render_template('delete.html', title='Delete Drink', form=form)
    form = DeleteForm(request.form)
    if form.validate_on_submit():
        recipes_db = mongo.db.recipes
        recipes_db.delete_one({
            '_id': ObjectId(recipe_id),
        })
        return redirect(url_for('home', title="Drink Deleted"))
    return render_template('delete.html', title="Delete Drink", recipe=recipe_db, form=form)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)