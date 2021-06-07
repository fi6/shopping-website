from flask import Flask

UPLOAD_FOLDER = 'shopping_website/static/images'

app = Flask(__name__)
app.config['SECRET_KEY'] = '#!#$@FDRWEWD@#fwdef'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_EXTENSIONS'] = ['jpg', 'png', 'gif']

from shopping_website import routes