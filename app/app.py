from flask import Flask, render_template,g, flash, redirect, url_for, session, request, logging
#from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from models import User,Recipe_category,Recipe,repository

USERS= []
recipe_categories =["food","ball","categories"]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# User Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = form.password.data

        user = User(username, email, password)
        # Commit to DB
        USERS.append(user)

        flash('You are now registered and can log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)



if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)