from flask import Flask
from api import app as MyApp
app = Flask(__name__)

print('creating app')
MyApp.create_app(app)

if __name__ == '__main__':
    print('running app')
    app.run(host='0.0.0.0', port=5000, debug=True)
