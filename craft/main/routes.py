from flask import render_template, url_for, request, redirect, session, flash, redirect, Blueprint


main = Blueprint('main', __name__)

@main.route("/")
def home():
    return render_template('index.html')

@main.route("/about")
def about():
    return render_template('about.html')

#@main.route("/contact")
#def contact():
    #return render_template('contact.html')



