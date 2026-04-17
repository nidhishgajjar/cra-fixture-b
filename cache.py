cache = {}

def get(key):
    return cache.get(key)


def put(key, value):
    cache[key] = value
