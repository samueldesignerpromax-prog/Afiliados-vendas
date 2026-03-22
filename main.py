from api.routes import app
from api.webhooks import webhook_bp

app.register_blueprint(webhook_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
