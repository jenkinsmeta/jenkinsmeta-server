import redis

REDIS = {
    'host': 'localhost',
    'port': 6379,
    'db': 0
}

CACHE_BACKEND = {
    'handler': redis.StrictRedis,
    'config': REDIS,
}

APP = {
    'host': '0.0.0.0',
    'port': 8080,
    'debug': True
}
