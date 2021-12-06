from flask import Flask, render_template

from data import homeData, experienceData, experienceData

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html', data = homeData)

@app.route('/experience')
def experience():
  for index in experienceData:
    print(experienceData[index])
  return render_template('experience.html', data = experienceData)

@app.route('/projects')
def projects():
  return render_template('projects.html', data = experienceData)