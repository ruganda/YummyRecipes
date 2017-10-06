from flask import Flask, render_template,g, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from models import User,Recipe
from functools import wraps

USERS= {}

recipes = {}
app = Flask(__name__)

class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])  
    confirm = PasswordField('Confirm Password')

class LoginForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField('Password', [
        validators.DataRequired(),validators.EqualTo('confirm', message='Passwords do not match')
    ])  

@app.route('/')
def home():
    return render_template('home.html')

# User Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = str(form.password.data)

        user = User(username, email, password)
        
        USERS[username] = user

        flash('You are now registered and can log in', 'success')
        return render_template('login.html')
    return render_template('register.html', form=form)
# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    password = form.password.data
    if request.method == 'POST':
        # Get Form Fields
        username = str(request.form['username'])
        password_candidate = str(request.form['password'])

        for user in USERS.values():
            if user.username == username and user.password == password_candidate:
                # Passed
                session['logged_in'] = True
                session['username'] = username
                flash('You are now logged in', 'success')
                
                return redirect(url_for('dashboard'))
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
    return render_template("login.html")
        

def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap
@app.route('/dashboard')
@is_logged_in
def dashboard ():
    return render_template('dashboard.html', recipes=recipes)



@app.route('/add_recipe', methods=['GET', 'POST'])
@is_logged_in
def add_recipe():
    if request.method == 'POST':
        recipes[request.form['title']] = Recipe(request.form['title'],request.form['description'])
        return render_template('dashboard.html', recipes=recipes)
    return redirect(url_for('dashboard'))


@app.route('/delete_recipe/<title>')
@is_logged_in
def delete_recipe(title):
    global recipes
    if title in recipes:
        del recipes[title]
    return redirect(url_for('dashboard'))


@app.route('/edit_recipe/<title>', methods=['GET', 'POST'])

def edit_recipe(title):
    global recipes
    recipe = recipes[title]

    if request.method == 'POST':
        recipe.recipe_title = request.form['title']
        recipe.recipe_description = request.form['description']
        
        return redirect(url_for('dashboard'))

    return render_template('edit_recipe.html', title = recipe.recipe_title, description = recipe.recipe_description)

@app.route('/recipe/<title>', methods=['GET', 'POST'])
@is_logged_in
def recipe_details(title):
    recipe = recipes[title]
    return render_template("details.html", title=recipe.recipe_title, description=recipe.recipe_description)



@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.secret_key='sfxhecygdzfzrettzxgvbdsjdbshbv123'
    app.run(debug=True)