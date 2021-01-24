import flask
import app


@app.route("/home")
def homepage():
    return "Welcome"

@app.route("/test-file-upload/", methods=["Get", "POST"])
def add_user():


    form = forms.SignupForm()

    if flask.request.method == "POST":

        if form.validate_on_submit():

            # Create a user
            user = models.User(
                name=form.username.data,
                age=form.age.data,
                password=form.password.data
            )

            if user.save():
                flask.flash(f"User {user.name} created successfully", category="success")
            else:
                flask.flash("Something went wrong..")

            return flask.redirect("/")

    return flask.render_template("signup.html", form=form)

@app.route("/sign-out/")
def signout():
    flask_login.logout_user()
    return flask.redirect("/")


@app.route("/sign-in/", methods=["GET", "POST"])
def signin():
    form = forms.SignInForm()

    if flask.request.method == "POST":
        if form.validate_on_submit():
            user = models.User.query.filter_by(name=form.username.data).first()

            if user.password == form.password.data:
                flask_login.login_user(user)
                flask.flash(f"Welcome {user.name}")
                return flask.redirect("/")
            else:
                flask.flash("Incorrect Username or Password")
    return flask.render_template("signin.html", form=form)
