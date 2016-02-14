from flask_restful import Resource, Api
from flask import Flask
import requests
import io
import redis
from jenkinsmeta_pb2 import computers_pb2, queue_pb2, views_pb2, view_pb2

app = Flask(__name__)
api = Api(app)


class Computers(Resource):
    def get(self):
        r = redis.StrictRedis(host='localhost', port=6379, db=0)
        self.host = 'localhost:5000'
        comp = computers_pb2.Computers()
        payload = r.get('computers')
        if not payload:
            payload = requests.get('http://'+self.host+'/computers').content
            r.setex('computers', 5, payload)
        comp.ParseFromString(payload)
        return r.get('computers')



api.add_resource(Computers, '/computers')

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5001, debug=True)

