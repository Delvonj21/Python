from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Cookie_order:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.cookie_type = data["cookie_type"]
        self.num_boxes = data["num_boxes"]

    @classmethod
    def get_one(cls, order_id):
        query = "SELECT * FROM cookie_orders WHERE id = %(id)s"
        order_dict = connectToMySQL("cookie_orders").query_db(query, {"id": order_id})
        order = Cookie_order(order_dict[0])

        return order

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cookie_orders;"
        all_orders_data = connectToMySQL("cookie_orders").query_db(query)
        orders = []
        for order in all_orders_data:
            orders.append(cls(order))

        return orders

    @classmethod
    def save(cls, data):
        query = "INSERT INTO cookie_orders (name, cookie_type, num_boxes) VALUES (%(name)s, %(cookie_type)s, %(num_boxes)s);"
        result = connectToMySQL("cookie_orders").query_db(query, data)
        return result

    @classmethod
    def edit(cls, data):
        query = "UPDATE cookie_orders SET name=%(name)s, cookie_type=%(cookie_type)s, num_boxes=%(num_boxes)s WHERE id = %(id)s;"
        result = connectToMySQL("cookie_orders").query_db(query, data)
        return result

    @staticmethod
    def validate_cookie_order(data):
        is_valid = True
        # check if each field is blank
        if len(data["name"]) == 0:
            flash("Name required.")
            is_valid = False
        if len(data["cookie_type"]) == 0:
            flash("Cookie Type required.")
            is_valid = False
        if len(data["num_boxes"]) == 0:
            flash("Number of boxes required.")
            is_valid = False
        # check if the number of cookies is positive
        elif int(data["num_boxes"]) <= 0:
            flash("Number of boxes must be a positive number.")
            is_valid = False

        return is_valid
