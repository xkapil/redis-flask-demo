import uuid

from flask_injector import inject
from services.redis import Redis

class Restaurant(object):
    @inject
    def post(self, restaurant: dict, lookup:Redis=None) -> dict:

        """ Store in Redis service """
        # Generates a unique ID for the restaurant
        id_str = str(uuid.uuid4())
        restaurant["id"] = id_str
        lookup.create(id_str, restaurant)
        return restaurant, 201

    @inject
    def get(self, id: str, lookup:Redis=None) -> dict:

        """ Lookup in Redis service """
        restaurant = lookup.get(id)
        return restaurant, 200

class_instance = Restaurant()