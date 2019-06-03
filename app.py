from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS


# init flask app
APP = Flask(__name__)
# ensure cors support
CORS(APP)
API = Api(APP)



class OfferCalculator(Resource):
    def get(self):
        args = request.args
        print(args)

        if args['arge'] == '26-35' and args['income'] == '$50k to $75k':
            return "Free Trip to Thailand"


API.add_resource(OfferCalculator, '/calculateoffer')


if __name__ == '__main__':
    APP.run(debug=True, threaded=True)
