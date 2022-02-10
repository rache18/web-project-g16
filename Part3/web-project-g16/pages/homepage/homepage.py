from flask import Blueprint, render_template, redirect, url_for ,session
from utilities.db.db_events import dbEvents

# homepage blueprint definition
homepage = Blueprint('homepage', __name__, static_folder='static', static_url_path='/homepage', template_folder='templates')


# Routes
@homepage.route('/')
def index():
    events= dbEvents.getEvents()
    print(events)
    return render_template('homepage.html',events=events)


@homepage.route('/homepage')
@homepage.route('/home')
def redirect_homepage():
    return redirect(url_for('homepage.index'))
