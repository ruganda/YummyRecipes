from flask import Flask, render_template,g, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from models import User,Recipe_category,Recipe
from functools import wraps

USERS= []
recipe_categories =["dinner","supper","lunch"]
recipes = []
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
        # Commit to DB
        USERS.append(user)

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

        for user in USERS:
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
    return render_template('dashboard.html', items=recipe_categories)

@app.route('/add_recipe_category', methods=['GET', 'POST'])
@is_logged_in
def add_recipe_category():
    global recipe_categories
    if request.method == 'POST':
        recipe_categories.append(request.form['item'])
        return render_template('dashboard.html', items=recipe_categories)
    return render_template('add_recipe_category.html')


@app.route('/remove/<name>')
@is_logged_in
def remove_item(name):
    global recipe_categories
    if name in recipe_categories:
        recipe_categories.remove(name)
    return redirect(url_for('dashboard'))

@app.route('/view_recipes')
@is_logged_in
def view_recipes():
    return render_template('view_recipes.html')



@app.route('/add_recipe', methods=['GET', 'POST'])
@is_logged_in
def add_recipe():
    global recipes
    if request.method == 'POST':
        recipes.append(request.form['item'])
        return render_template('view_recipes.html', items=recipes)
    return render_template('add_recipe.html')


@app.route('/delete_recipe/<recipe>')
@is_logged_in
def delete_recipe(recipe):
    global recipes
    if recipe in recipes:
        recipes.remove(recipe)
    return redirect(url_for('view_recipes'))

@app.route('/details', methods=['GET', 'POST'])
@is_logged_in
def add_details():
    global recipes
    if request.method == 'POST':
        recipes.append(request.form['item'])
        return render_template('detail.html', items=recipes)
    return render_template('add_detail.html')

@app.route('/details')
@is_logged_in
def details():
    all_recipes = []
    return render_template('details.html', recipes=all_recipes)



@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.secret_key='sfxhecygdzfzrettzxgvbdsjdbshbv123'
    app.run(debug=True)