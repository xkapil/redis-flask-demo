import redis

class Redis(object):
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.client = None

    def get_client(self) -> redis.StrictRedis:
        if self.client is None:
            self.client = redis.StrictRedis(self.host, self.port, db=0)
        return self.client

    def create(self, key, value):
        redis_client = self.get_client()
        if not redis_client.exists(key):
            redis_client.set(key, value)
        return True

    def get(self, key):
        redis_client = self.get_client()
        if redis_client.exists(key):
            return redis_client.get(key)
        return None
