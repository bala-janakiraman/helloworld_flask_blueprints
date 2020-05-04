from flask import Flask
from apis.routes.routes import mod

app = Flask(__name__)

# Register the blueprint
app.register_blueprint(mod)
