from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  informations = {
    "title": "Lucas Braz Dias",
    "textContent": "Meu nome é Lucas, tenho dezenove anos,\
      atualmente estou cursando o curso de\
      Desenvolvimento de Software Multiplataforma\
      pela Fatec de São José dos Campos.\
      Tenho dois técnicos na área de TI\
      e atualmente sou Desenvolvedor FullStack",
    "socialLinks": {
      "github": "https://github.com/lucasbdias",
      "linkedin": "https://www.linkedin.com/in/lucas-braz-dias/",
      "email": "mailto:lucasbrzdias@gmail.com"
    }
  }
  return render_template('index.html', data = informations)

@app.route('/experience')
def experience():
  return render_template('experience.html')

@app.route('/projects')
def projects():
  return render_template('projects.html')