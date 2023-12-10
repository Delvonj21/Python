from flask_app import app
from flask import render_template, session, redirect, request
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask import flash


@app.route("/recipes/home")
def recipes_home():
    if "user_id" not in session:
        flash("You must be logged in to access the dashboard.")
        return redirect("/")

    user = User.get_by_id(session["user_id"])

    # get all the recipes and send to the template
    recipes = Recipe.get_all()
    return render_template("home.html", user=user, recipes=recipes)


# render page details for one recipe
@app.route("/recipes/<recipe_id>")
def recipe_details(recipe_id):
    recipe = Recipe.get_one_by_id(recipe_id)

    # pass recipe into template
    return render_template("recipe_detail.html" recipe=recipe)


# render page with create form
@app.route("/recipes/new")
def create_page():
    print("In create route.")
    return render_template("create_recipe.html")


# render page with edit form
@app.route("/recipes/edit/<recipe_id>")
def edit_page(recipe_id):
    recipe = Recipe.get_one_by_id(recipe_id)
    # need to get that recipe from the database

    # pass recipe into template
    return render_template("edit_recipe.html", recipe=recipe)


@app.route("/recipes/delete/<recipes_id>")
def delete_recipe(recipe_id):
    print("In delete page", recipe_id)

    Recipe.delete_by_id(recipe_id)
    return redirect("/recipes/home")


@app.route("/recipes", methods=["POST"])
def create_recipe():
    # Before save
    # pass the form data into a validator
    is_valid = Recipe.is_valid(request.form)

    # if the form data is good THEN save and go to home

    if is_valid:
        Recipe.save(request.form)
        return redirect("/recipes/home")

    return redirect("/recipes/new")


@app.route("/recipes/update")
def update_recipe():
    is_valid = Recipe.is_valid(request.form)

    if is_valid:
        Recipe.update(request.form)
        return redirect("/recipes/home")
    return redirect(f"/recipes/edit/{request.form['id']}")
