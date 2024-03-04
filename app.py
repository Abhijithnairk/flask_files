from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/profile/about')

def about():
    return '<h1>This is About page'

@app.route('/profile/<username>')

def abhi(username):
    return render_template('profile.html',username=username)

app.run(debug=True)