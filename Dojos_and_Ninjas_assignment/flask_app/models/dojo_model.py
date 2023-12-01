
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app.models import ninja_model
# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, flask-bcrypt should already be in your env check the pipfile

# Remember 'fat models, skinny controllers' more logic should go in here rather than in your controller. Your controller should be able to just call a function from the model for what it needs, ideally.

class Dojo:
    db = "dojos_and_ninjas" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
        # What changes need to be made above for this project?
        #What needs to be added here for class association?

    def __repr__(self) -> str:
        return f"Dojo Repr --> {self.id} {self.name}; Ninjas {self.ninjas}"
    
    @classmethod
    def save(cls, data):
        query = """INSERT INTO dojos (name)
                VALUES ( %(name)s)
                """
        return connectToMySQL("dojos_and_ninjas").query_db(query, data)

    @classmethod
    def get_one(cls, dojo_id):
        query  = "SELECT * FROM dojos WHERE id = %(id)s;"
        data = {'id': dojo_id}
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL("dojos_and_ninjas").query_db(query)
        print('dojo_results',results) 
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def get_dojo_with_ninjas(cls,dojo_id):
        data = {
            "id" : dojo_id
        }
        query = """SELECT * FROM dojos 
                LEFT JOIN ninjas on ninjas.dojo_id = dojos.id 
                WHERE dojos.id = %(id)s;
                """  
        results = connectToMySQL("dojos_and_ninjas").query_db(query,data)
        dojo_result = cls(results[0])
        for ninja_in_dojo in results:
            ninja_one_dojo = {
                "id": ninja_in_dojo["ninjas.id"],
                "dojo_id": ninja_in_dojo["dojo_id"],
                "first_name": ninja_in_dojo["first_name"],
                "last_name": ninja_in_dojo["last_name"],
                "age": ninja_in_dojo["age"],
                "created_at": ninja_in_dojo["ninjas.created_at"],
                "updated_at": ninja_in_dojo["ninjas.updated_at"],
            }
            dojo_result.ninjas.append(ninja_model.Ninja(ninja_one_dojo))
        return dojo_result

    # Create Users Models



    # Read Users Models



    # Update Users Models



    # Delete Users Models