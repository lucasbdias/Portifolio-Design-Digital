 # Portifólio


- [📝 Objetivo](#📝-Objetivo)
- [✔ Requisitos](#📝-Objetivo)
- [⚙️ Tecnologias](#⚙️-Tecnologias)
- [📦 Arquitetura](#📦-Arquitetura)
- [📥 Instalação](#📥-Instalação)
- [🔗 Entregas](#🔗-Entregas)
- [📤 Vídeos](#📤-Vídeos)

# 📝 Objetivo

Desenvolvimento de um sistema para Internet que sirva como uma página pessoal onde possam ser encontradas as seguintes informações:
 1. Dados do proprietário do sistema (autor da página/aplicação web); <br/>
    a. Uma foto que contenha efeitos de redimensionamento e filtro;
    <br/>
    b. Informações educacionais;
    <br/>
    c. Outras informações pertinentes (interesses, etc.). 
  2. Portfólio (trabalhos desenvolvidos ou que pretende desenvolver); 
  3. Outras informações relevantes ou de interesse do autor/proprietário. 

# ✔ Requisitos

- [x]  Responsividade de maneira a manter um layout amigável e bem estruturado tanto em um computador de mesa (desktop, laptop e similares) como em um dispositivo móvel;
- [x]  Boas  práticas  de  arquitetura  de  informação  na  construção  das interfaces;
- [x]  Possuir no mínimo, três interfaces acessíveis a partir de algum mecanismo de navegação;
- [x]  Possuir um esquema de cores e layout único com relação aos demais sistemas desenvolvidos  pelos  seus  colegas  de  turma;
- [x]  Fazer  uso  de  arquivo  de  fonte  externa,  disponibilizado  pelo  servidor  da aplicação, sendo que a tipografia deve ser adequada à natureza do uso escolhido;
- [x]  Conter ao menos uma imagem ou logotipo que seja único e que contribua para dar uma identidade visual ao mesmo;
- [x]  Deve  aplicar  a  tecnologia/conceito  de utilização  de  arquivos  de  imagens responsivas. 

# ⚙️ Tecnologias

<img align="center" alt="HTML5" src="https://img.shields.io/badge/HTML5-DD4C2D?style=for-the-badge&logo=html5&logoColor=white"/>
<img align="center" alt="CSS3" src="https://img.shields.io/badge/CSS3-0070BB?style=for-the-badge&logo=css3&logoColor=white"/>
<img align="center" alt="Python" src="https://img.shields.io/badge/Python-FFCB3A?style=for-the-badge&logo=python&logoColor=white"/>
<img align="center" alt="Flask" src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"/>

# 📦 Arquitetura

```shell
src/
|-- static/ # Contém os arquivos de estilização, fontes e imagens.
  -- static/assets/ # Contém apenas as fontes e imagens.
  -- static/css/ # Contém apenas as estilizações.
|-- templates/ # Diretório que contém os arquivos html.
|-- data/ # Contém os dados das páginas.
|-- bin/ # Shell script de execução.
```

# 📥 Instalação

**Você vai necessitar do [GIT](https://git-scm.com/book/pt-br/v2/Come%C3%A7ando-Instalando-o-Git) e [Python](https://www.python.org/downloads/), então clone o repo, utilizando este comando:**

```bash
git clone https://github.com/lucasbdias/Portifolio-Design-Digital.git
```
Criar ambiente virtual Python:
```bash
python3 -m venv env
```

Iniciar ambiente:

Para Windows:
```bash
.\env\Scripts\activate
```

Para Linux:
```bash
source env/bin/activate
```

Instalar dependencias:
```bash
pip3 install -r requirements.txt
```

Executar aplicação:
```bash
python3 src/wsgi.py
```

# 🔗 Entregas

| Data | Links |
| ------ | ------ |
|    22/09/2021    |[Entrega 01](https://github.com/lucasbdias/Portifolio-Design-Digital/releases/tag/entrega01)|
|    15/11/2021    |[Entrega 02](https://github.com/lucasbdias/Portifolio-Design-Digital/releases/tag/entrega02)|
|    06/12/2021    |[Entrega Final](https://github.com/lucasbdias/Portifolio-Design-Digital/releases/tag/entrega-final)|

# 📤 Vídeos
| Data | Links |
| ------ | ------ |
|    22/09/2021    |[Vídeo 01](https://youtu.be/dNyMI2Xg6-Q)|
|    15/11/2021    |[Vídeo 02](https://youtu.be/VStRj76jTow)|
