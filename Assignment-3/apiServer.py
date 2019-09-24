from flask import Flask, jsonify
from flask_restful import Resource, Api, request


app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        json_data = request.get_json(force=True)
        print(json_data)
        return {'MathResult':str((int(json_data['key1']) + int(json_data['key2']))) }

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)












