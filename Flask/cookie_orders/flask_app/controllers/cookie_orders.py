from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.cookie_order import Cookie_order


@app.route("/")
@app.route("/cookies")
def index():
    all_orders = Cookie_order.get_all()
    return render_template("cookies.html", orders=all_orders)


@app.route("/cookies/new")
def new_cookies():
    return render_template("new_order.html")


@app.route("/cookies/edit/<int:order_id>")
def edit_cookies(order_id):
    cookie_order = Cookie_order.get_one(order_id)

    return render_template("edit_order.html", cookie_order=cookie_order)


# POST (ACTION) ROUTES
@app.route("/cookies/create", methods=["POST"])
def create_order():
    if Cookie_order.validate_cookie_order(request.form):
        Cookie_order.save(request.form)
        return redirect("/cookies")
    return redirect("/cookies/new")


@app.route("/cookies/update", methods=["POST"])
def update_order():
    if Cookie_order.validate_cookie_order(request.form):
        Cookie_order.edit(request.form)
        return redirect("/cookies")
    return redirect(f"/cookies/edit/{request.form['id']}")
