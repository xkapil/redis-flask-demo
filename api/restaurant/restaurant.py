import uuid

from flask_injector import inject
from services.redis import Redis

class Restaurant(object):
    @inject
    def post(self, restaurant: dict, lookup:Redis=None) -> dict:

        """ Store in Redis service """
        # TODO
        # Generates a unique ID for the restaurant
        restaurant['id'] = str(uuid.uuid4())
        print("redis.name %s" % lookup.redis_name)

        return restaurant, 201

    @inject
    def get(self, id: str, lookup:Redis=None) -> dict:

        """ Lookup in Redis service """
        # TODO
        # restaurant = lookup.get(id)
        restaurant = dict()
        restaurant["id"] = id
        return restaurant, 200

# TODO Can we comment this?
class_instance = Restaurant()