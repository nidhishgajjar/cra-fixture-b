import time

cache = {}

def get(key):
    entry = cache.get(key)
    if entry is None:
        return None
    value, expiry = entry
    if expiry < time.time():
        del cache[key]
        return None
    return value


def put(key, value, ttl_seconds=60):
    expiry = time.time() + ttl_seconds
    cache[key] = (value, expiry)


def evict_expired():
    now = time.time()
    for k in list(cache.keys()):
        if cache[k][1] < now:
            del cache[k]
