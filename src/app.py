from flask import Flask, render_template

from .data import homeData

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html', data = homeData)

@app.route('/experience')
def experience():
  return render_template('experience.html')

@app.route('/projects')
def projects():
  return render_template('projects.html')