from flask import Flask, request, abort
from cache import Cache
import requests
import settings
import redis


app = Flask(__name__)
cache = Cache(app)


@app.route('/hosts', methods=['POST', 'GET', 'DELETE'])
def hosts():
    url = request.form.get('url')
    hosts_key = 'hosts'
    if request.method == 'GET':
        return str(request.cache.lrange(hosts_key, 0, -1))
    if request.method == 'POST':
        if not url: abort(400)
        request.cache.lrem(hosts_key, 0, url)
        request.cache.rpush(hosts_key, url)
    if request.method == 'DELETE':
        if not url: abort(400)
        request.cache.lrem(hosts_key, 0, url)
    return request.method

@app.route('/<path:path>')
def proxy(path):
    return str('Requested path: {}'.format(path))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

