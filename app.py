from flask import Flask
from views import view_blueprint

app = Flask(__name__)

app.register_blueprint(view_blueprint, url_prefix="/",  static_url_path='/static')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')