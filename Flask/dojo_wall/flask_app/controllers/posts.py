from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.post import Post


@app.route("/posts", methods=["POST"])
def create_post():
    Post.save(request.form)
    return redirect("/wall")


@app.route("/posts/delete/<int:post_id>")
def delete_post(post_id):
    Post.delete(post_id)
    return redirect("/wall")
