from flask import Flask, jsonify
from flask_restful import Resource, Api, request


app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        json_data = request.get_json(force=True)
        n1 = float(json_data['key1'])
        n2 = float(json_data['key2'])
        operator = json_data['operator']
        
        if operator == '+':
            return {'MathResult':str(n1 + n2) }
        elif operator == '-':
            return {'MathResult':str(n1 - n2) }
        elif operator == '*':
            return {'MathResult':str(n1 * n2) }
        elif operator == '/':
            if n2 != 0.0:
                return {'MathResult':str(n1 / n2) }
            else:
                return {'MathResult':'Illegal n2 for a divide!' }
        else:
            return {'MathResult':'Invaild operator' }

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)












