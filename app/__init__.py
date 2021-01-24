import os
import flask_login
#
# __init__.py
#

import flask
import flask_sqlalchemy
import flask_migrate


basedir = os.path.abspath(os.path.dirname(__file__))

# Create the app controller
app = flask.Flask(__name__)

# App config
app.config["SECRET_KEY"] = "edwoijfwoqijer"


app.config["UPLOAD_DIR"] = os.path.join(basedir, "uploads") # uploads/ need to exist

# Format of the URL: postgres://<username>:<password>@localhost:5432/<db name>

app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://postgres:postgres@localhost:5432/gam"

# Create the virtual database
db = flask_sqlalchemy.SQLAlchemy(app)    # |>
migrate = flask_migrate.Migrate(app, db) # |>  These lines will always be the same

login_manager = flask_login.LoginManager(app)

# END OF FILE

from . import routes, models

@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(user_id)