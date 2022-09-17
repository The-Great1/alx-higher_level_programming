#!/usr/bin/python3
"""The base class"""
import json


class Base:
    """This is the class definition"""
    __nb_objects = 0

    def __init__(self, id=None):
        """This is the class initialiser"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """This returns the json representation of list_dictionaries"""
        if list_dictionaries is None:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """This writes the json string representation of list_objs
        to a file"""
        name = cls.__name__ + ".json"
        with open(name, 'w', encoding='utf-8') as den:
            if list_objs is None:
                den.write("[]")
            else:
                json_rep = []
                for item in list_objs:
                    json_rep.append(item.to_dictionary())
                den.write(cls.to_json_string(json_rep))

    @staticmethod
    def from_json_string(json_string):
        """This returns the list of the json string representation
        'json_string'
        Args:
            json_string: Is a string representatng a list of dictionaries
        Returns: an empty list if json_string is None
                otherwise returns the list represented by json_string"""

        if json_string is None or len(json_string) == 0:
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """This returns an instance with all attributes already set
        Args:
            **dictionary is a double pointer to a dictionary
        A dummy instance must first be created with mandatory attributes
        Then the 'update' method must be used to set the attributes
        **dictionary must be used as **kwargs of the method 'update'
        """
        if dictionary is not None and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy_instance = cls(1, 1)
            elif cls.__name__ == "Square":
                dummy_instance = cls(1)

            dummy_instance.update(**dictionary)
            return dummy_instance

    @classmethod
    def load_from_file(cls):
        """This returns a list of instances"""
        name = cls.__name__ + ".json"

        with open(name) as f:
            try:
                content = f.read()
                dicts = Base.from_json_string(content)
                sol_list = []
                for item in dicts:
                    sol_list.append(cls.create(**item))
                return (sol_list)
            except IOError:
                return ([])
