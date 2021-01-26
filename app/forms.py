import flask_wtf
import wtforms

class SignupForm(flask_wtf.FlaskForm):

    username = wtforms.StringField("Username: ")
    password = wtforms.PasswordField("Password: ")

    submit  = wtforms.SubmitField("Sign up")


class SignInForm(flask_wtf.FlaskForm):
    username = wtforms.StringField("Username: ")
    password = wtforms.PasswordField("Password: ")

    submit = wtforms.SubmitField("Sign In")
