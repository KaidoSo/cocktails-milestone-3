import os
from flask import Flask, render_template, redirect, request, url_for
from forms import RegistrationForm, LoginForm
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.confi['SECRET_KEY'] = ''
app.config["MONGO_DBNAME"] = 'cocktails'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-9apc7.mongodb.net/cocktails?retryWrites=true&w=majority'

mongo = PyMongo(app)



@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("home.html", recipes=mongo.db.recipes.find())

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('register.html', title='Log In', form=form)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)