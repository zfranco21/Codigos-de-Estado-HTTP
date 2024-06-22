from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:losceibos@localhost/zfranco21'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.static_folder = 'static'

class Code(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(10), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    imagen = db.Column(db.String(200), nullable=False)
    descripcion = db.Column(db.String(500), nullable=False)

    def __init__(self, numero, nombre, imagen, descripcion):
        self.numero = numero
        self.nombre = nombre
        self.imagen = imagen
        self.descripcion = descripcion

    def __repr__(self):
        return f'<Code {self.numero} - {self.nombre}>'

@app.route('/')
def index():
    codes = Code.query.all()
    return render_template('index.html', codes=codes)

@app.route('/search')
def search_codes():
    numero = request.args.get('numero', '')

    if numero:
        codes = Code.query.filter_by(numero=numero).all()
    else:
        codes = Code.query.all()

    return render_template('index.html', codes=codes)

@app.route('/codigo/<int:codigo_id>')
def codigo(codigo_id):
    code = Code.query.get(codigo_id)
    if not code:
        return "Código de estado no encontrado", 404
    return render_template('codigo.html', code=code)


if __name__ == '__main__':
    app.run(debug=True)
