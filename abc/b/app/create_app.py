from flask import Flask

def create_app():
    app = Flask(__name__)
    # app.run(host="0.0.0.0", use_reloader=False)
    @app.route("/")
    def index():
        return "Flask app B"
    
    return app