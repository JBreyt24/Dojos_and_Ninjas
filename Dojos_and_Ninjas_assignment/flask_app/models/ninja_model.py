
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, flask-bcrypt should already be in your env check the pipfile

# Remember 'fat models, skinny controllers' more logic should go in here rather than in your controller. Your controller should be able to just call a function from the model for what it needs, ideally.

class Ninja:
    db = "dojos_and_ninjas" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.dojo_id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # What changes need to be made above for this project?
        #What needs to be added here for class association?

    def __repr__(self) -> str:  #this is optional to help debug
        return f" Ninja Repr - -> {self.id} {self.dojo_id} {self.first_name}"

    @classmethod
    def save(cls, data):
        query = """INSERT INTO ninjas (dojo_id, first_name, last_name,
                age)
                VALUES ( %(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s);
                """
        return connectToMySQL("dojos_and_ninjas").query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL("dojos_and_ninjas").query_db(query)
        print(results)       
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninja
    
    @classmethod
    def get_ninja_dojo(cls, data):
        query = """SELECT dojo_id FROM
                ninjas WHERE id = %(id)s;
                """
        query_data = {
            "id" : data
        }
        dojo_dict = connectToMySQL("dojos_and_ninjas").query_db(query, query_data)
        return dojo_dict[0]['dojo_id']


    # Create Users Models



    # Read Users Models



    # Update Users Models



    # Delete Users Models