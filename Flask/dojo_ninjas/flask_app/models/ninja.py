from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (dojo_id, first_name, last_name, age) VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s);"
        result = connectToMySQL("dojo_ninjas").query_db(query, data)
        return result

    @classmethod
    def get_one_by_id(cls, ninja_id):
        query = "SELECT * FROM ninjas WHERE id = %(ninja_id)s"
        data = {"ninja_id": ninja_id}
        result_list = connectToMySQL("dojo_ninjas").query_db(query, data)
        ninja = cls(result_list[0])
        return ninja

    @classmethod
    def delete_by_id(cls, ninja_id):
        query = "DELETE FROM ninjas WHERE id = %(ninja_id)s;"
        data = {"ninja_id: ninja_id"}
        connectToMySQL("dojo_ninjas").query_db(query, data)
        return ninja_id

    @classmethod
    def update(cls, data):
        query = "UPDATE ninjas SET first_name=%(first_name)s, last_name=%(last_name)s, age=%(age)s "

        connectToMySQL("dojo_ninjas").query_db(query, data)
        return
