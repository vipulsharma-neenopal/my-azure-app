import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    secret = os.environ.get("DB_PASSWORD")
    return f"Retrieved Secret: {secret}"