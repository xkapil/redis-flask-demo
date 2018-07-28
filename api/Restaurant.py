import uuid

from flask_injector import inject

class Restaurant(object):
    @inject(lookup=Redis)
    def post(self, lookup, restaurant: dict) -> dict:

        """ Store in Redis service """
        # TODO
        # Generates a unique ID for the restaurant
        restaurant.id = str(uuid.uuid4())

        return restaurant, 201

    @inject(lookup=Redis)
    def get(self, lookup, id: str) -> dict:

        """ Lookup in Redis service """
        # TODO
        restaurant = lookup.get(id)
        return restaurant, 200

# TODO Can we comment this?
class_instance = Restaurant()