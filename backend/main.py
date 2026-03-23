import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask
from flask_cors import CORS
from api.webhooks import webhook_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(webhook_bp)

@app.route('/')
def index():
    return {"message": "API da Plataforma de Cursos", "status": "online"}

from api.routes import *

if __name__ == '__main__':
    app.run(debug=True, port=5000)
