from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app.models import user
import re

class Recipe:
  def __init__(self, recipe):
    self.id = recipe["id"]
    self.name = recipe["name"]
    self.description = recipe["description"]
    self.instructions = recipe["instructions"]
    self.date_made = recipe["date_made"]
    self.under_30 = recipe["under_30"]
    self.created_at = recipe["created_at"]
    self.updated_at = recipe["updated_at"]
    self.user = None

  @classmethod
  def save(cls, recipe_data):
    query = "INSERT INTO recipes(name, description, instructions, date_made, under_30) VALUES(%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under_30)s);"
    connectToMySQL('recipes').query_db(query, recipe_data)
    return True
  
  @classmethod
  def get_one_by_id(cls,recipe_id):
    query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id WHERE recipes.id = %(id)s;"
    data = {
      "id":recipe_id
    }
    recipe_dict = connectToMySQL('recipes').query_db(query,data)[0]

    recipe_obj = Recipe(recipe_dict)
    user_obj = user.User({
      "id":recipe_dict["user.id"],
      "first_name":recipe_dict["first_name"],
      "last_name":recipe_dict["last_name"],
      "email":recipe_dict["email"],
      "create_at":recipe_dict["users.created_at"],
      "updated_at":recipe_dict["users.updated_at"]
    })
    recipe_obj.user = user_obj
    return recipe_obj
  
  @classmethod
  def get_all(cls):
    query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;"
    results = connectToMySQL('recipes').query_db(query)
    recipes = []

    for recipe_dict in results:
      recipe_obj = Recipe(recipe_dict)
      user_obj = user.User({
          "id":recipe_dict["user.id"],
          "first_name":recipe_dict["first_name"],
          "last_name":recipe_dict["last_name"],
          "email":recipe_dict["email"],
          "create_at":recipe_dict["users.created_at"],
          "updated_at":recipe_dict["users.updated_at"]
      })
      recipe_obj.user = user_obj

      recipes.append(recipe_obj)

      return recipes
    
    @classmethod
    def delete_by_id(cls,recipe_id):
      query = "DELETE FROM recipes WHERE id = %(id)s;"
      data = {
        "id":recipe_id
      }
      connectToMySQL('recipes').query_db(query,data)
      return
    
    @classmethod
    def update(cls,recipe_data):
      query = "UPDATE recipes SET name = %(name)s, description=%(description)s, instructions= %(instructions)s, date_made=%(date_made)s, under_30=%(under_30)s WHERE id=%(id)s"

      connectToMySQL('recipes').query_db(query, recipe_data)
      return
    
    @staticmethod
    def is_valid(recipe_dict):
      is_valid = True

      if len(recipe_dict["name"]) == 0:
        is_valid = False
        flash ("Name is required.")
      if len(recipe_dict["description"]) == 0:
        is_valid = False
        flash ("Description is required")
      elif len(recipe_dict["description"]) < 3:
        is_valid = False
        flash ("Description must be at least 3 characters ")

      if len(recipe_dict["instructions"]) == 0:
        is_valid = False
        flash ("Instructions is required")
      elif len(recipe_dict["instructions"]) < 3:
        is_valid = False
        flash ("Instructions must be at least 3 characters ")
      if len(recipe_dict["date_made"]) == 0:
        is_valid = False
        flash ("Date Made is required")
      if "under_30" not in recipe_dict:
        is_valid = False
        flash ("Recipe length required")
      
     
