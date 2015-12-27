from flask import Flask
from flask_restful import Resource, Api

import resources

app = Flask(__name__)
api = Api(app)

api.add_resource(resources.Quote, "/quote/random")


if __name__ == '__main__':
        app.run(debug=True)
