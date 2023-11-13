from flask import render_template, request, redirect

from flask_app import app

from user import User


@app.route("/")
def index():
    return redirect("/users")


@app.route("/users")
def users():
    return render_template("users.html", users=User.get_all())


@app.route("/user/new")
def new():
    return render_template("new_user.html")


@app.route("/user/create", methods=["POST"])
def create():
    # check if the form info is valid
    if User.valid_user(request.form):
        User.save(request.form)
        return redirect("/")
    # if not - send direct the user back to the create page
    else:
        return redirect("/user/new")


@app.route("/user/edit/<int:id>")
def edit(id):
    data = {"id": id}
    return render_template("edit_user.html", user=User.get_one(data))


@app.route("/user/show/<int:id>")
def show(id):
    data = {"id": id}
    return render_template("show_user.html", user=User.get_one(data))


@app.route("/user/update", methods=["POST"])
def update():
    User.update(request.form)
    return redirect("/users")


@app.route("/user/remove/<int:id>")
def remove(id):
    data = {"id": id}
    User.remove(data)
    return redirect("/users")
