from flask import Flask
# from Flask_RESTful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


@app.route("/main")
def hello_world():
    return "<p>hello world</p>"


class DemoApiEndpoint(Resource):
    def __init__(self):
        self.post_args = reqparse.RequestParser()
        self.post_args.add_argument("name",
                                    type=str,
                                    help="you must include a name string with this post request.",
                                    required=True)

    def get(self):
        return {
            "message": "This is a response from a get request"
        }

    def post(self):
        return {

        }