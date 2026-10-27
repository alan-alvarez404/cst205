from flask_bootstrap import Bootstrap4
from flask import Flask, render_template

# Task 1: Hello World - Create a "Hello World" Flask application and display three acronyms and what they mean
print('Task 1: Hello World - Create a "Hello World" Flask application and display three acronyms and what they mean')

# create an instance of Flask
app = Flask(__name__)

bootstrap = Bootstrap4(app)

# route decorator binds a function to a Url
@app.route('/')
def three_favorite_acronyms():

    # Each classmate's first name and acronym in a separate HTML paragraph (<p></p>)
    return '''
    <p>Rishabh: POS (Point of Sale) </p>
    <p>Daniel: LOL (League of Legends) </p>
    <p>Ethan: GG WP (Good game, well played) </p>
    '''

print()
# Task 3: Add Templates - Create a new route to call render_template() and pass in favorite acronym as python variable
print('Task 3: Add Templates - Create a new route to call render_template() and pass in favorite acronym as python variable')

# Adding new route to call my_favorite_acronym() and pass in favorite acronym as python variable
@app.route('/alan')
def my_favorite_acronym():
    return render_template('template.html', acronym ='LMAO') # To be displayed using Jinja's {{ }} syntax

print()
# Task 4: Add Bootstrap - Use Bootstrap classes text-center, rounded, and w-50 to center the image, git it rounded corners, and set its width
print('Task 4: Add Bootstrap - Use Bootstrap classes text-center, rounded, and w-50 to center the image, git it rounded corners, and set its width')

# Adding new route to call open_image() to open an image
@app.route('/image')
def open_image():
    return render_template('image.html')
