from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Updated via CI/CD 🚀"

if __name__ == "__main__":
    app.run()