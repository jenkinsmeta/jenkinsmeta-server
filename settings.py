import redis

REDIS = {
    'host': 'localhost',
    'port': 6379,
    'db': 0
}

CACHE_BACKEND = {
    'handler': redis.StrictRedis,
    'config': REDIS,
    'hosts_key': 'hosts'
}
