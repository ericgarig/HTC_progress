"""Main app file."""
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')


db = SQLAlchemy(app)
migrate = Migrate(app, db)


from views import vd, vg, vi, vt, vw, v_debug, v_sheet
from models import *


# blueprints
app.register_blueprint(vd, url_prefix='/daily')
app.register_blueprint(vg, url_prefix='/goal')
app.register_blueprint(vi, url_prefix='/interruption')
app.register_blueprint(vt, url_prefix='/task')
app.register_blueprint(vw, url_prefix='/week')
app.register_blueprint(v_debug, url_prefix='/debug')
app.register_blueprint(v_sheet, url_prefix='')


if __name__ == '__main.py__':
    app.run()
