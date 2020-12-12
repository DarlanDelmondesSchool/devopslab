from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

crsf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "Lab Pipeline DevOps"

if __name__ == '__main__':
    app.run(debug=True)