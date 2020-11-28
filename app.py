from flask import Flask
fom flask_wtf.csrf import CSRFProtect


app = Flask(__name__)


crsf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "Laboratório Pipeline DevOps"
if __name__ == '__main__':
    app.run(debug=True)
