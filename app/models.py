import flask_login

from . import db

class User(db.Model, flask_login.UserMixin):

    id   = db.Column(db.Integer(), primary_key=True) # This column will be the same

    name = db.Column(db.String(64), nullable=False, unique=True)
    age  = db.Column(db.Integer())

    password = db.Column(db.String(), nullable=True)

    def save(self):
        db.session.add(self)
        # Commit the changes
        try:
            db.session.commit()
            return True

        except:
            # Something went wrong --> rollback
            db.session.rollback()
            return False

