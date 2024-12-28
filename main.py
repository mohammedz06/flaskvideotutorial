from flask import Flask, render_template, url_for, request, session, redirect, session

app = Flask(__name__)

app.secret_key = "Hello"

@app.route("/")
def main():
    if "user" not in session:
        user_logged_in = "user" in session
        return render_template("home.html", user_logged_in = user_logged_in)
    else:
        return redirect(url_for("user"))




@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":

        session.permanent = True
        user = request.form["nm"]

        session["user"] = user

        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))

    return render_template("signin.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        user_logged_in = True
    
        return render_template("home.html", user = user, user_logged_in = user_logged_in)
    else:
        return redirect(url_for("login"))


@app.route("/resume")
def resume():
    if "user" in session:
        user = session["user"]
        return render_template("resume.html")
    else:
        return redirect(url_for("login"))


@app.route("/wrapped")
def wrapped():
    if "user" in session:
        user = session["user"]
        return render_template("wrapped.html")
    else:
        return redirect(url_for("login"))

@app.route("/books")
def books():
    if "user" in session:
        user = session["user"]
        return render_template("books.html")
    else:
        return redirect(url_for("login"))
    
@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]

    session.pop("user", None)

    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(port = 8000, debug = True)

