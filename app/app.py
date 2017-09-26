from flask import Flask, render_template,g, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from models import User,Recipe_category,Recipe,repository

USERS= []
recipe_categories =["food","ball","categories"]

app = Flask(__name__)



if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)