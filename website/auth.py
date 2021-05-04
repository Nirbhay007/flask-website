from flask import Blueprint, render_template, request, flash

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=['POST', 'GET'])
def login():
    data = request.form
    print(data)
    return render_template("login.html",)


@auth.route("/logout")
def logout():
    return "<h1>Logout</h1>"


@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        firstname = request.form.get("firstname")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if len(email) < 4:
            flash("Email must be greater than 3 chars", category='error')

        elif len(firstname) < 2:

            flash("First name must be greater than 1 chars", category='error')
        elif password1 != password2:
            flash("Passwords don\'t match", category='error')
        elif len(password1) < 7:

            flash("Password should be more than 7 chars.", category='error')
        else:
            # add user to database
            flash("Account Created", category='success')

    return render_template("sign_up.html")
