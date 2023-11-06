from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import dojo, ninja


@app.route("/ninjas")
def ninjas():
    return render_template("ninja.html", dojos=dojo.Dojo.get_all())


@app.route("/create/ninja", methods=["POST"])
def create_ninja():
    ninja.Ninja.save(request.form)
    return redirect("/")


@app.route("/ninjas/edit/<ninja_id>")
def edit_page(ninja_id):
    ninja.Ninja.get_one_by_id(ninja_id)
    return render_template("edit_ninja.html", ninja=ninja)


@app.route("/ninjas/delete/<ninja_id>/<dojo_id>")
def delete_ninja(ninja_id, dojo_id):
    ninja.Ninja.delete_by_id(ninja_id)
    return redirect(f"/dojo/{dojo_id}")


@app.route("/ninjas/update", methods=["POST"])
def update_ninja():
    ninja.Ninja.update(request.form)
    return redirect(f'/dojo/{request.form["dojo_id"]}')
