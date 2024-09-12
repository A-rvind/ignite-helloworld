from flask import Flask, request, jsonify, make_response
from flask_smorest import Api, Blueprint
from flask_restful import Resource
from flask_cors import CORS
import uuid

app = Flask(__name__)
CORS(app) # here cors is used python code with html smoothly
#Enable cors 
app.config["API_TITLE"] = "Hello World API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.0"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

# Given condition of hello world in different lang..
greetings = {
    "English": "Hello world",
    "French": "Bonjour le monde",
    "Hindi": "Namastey sansar"
}

blp = Blueprint(
    "hello_world", "hello_world", url_prefix="/hello",
    description="Operations on Hello World messages"
)

@blp.route('/')
class HelloWorld(Resource):
    def get(self):
        language = request.args.get('language')
        if not language or language not in greetings:
            return make_response(
                jsonify({"error_message": "The requested language is not supported"}),
                400
            )
        
        response = {
            "ID": str(uuid.uuid4()),
            "msgText": greetings[language]
        }
        return make_response(jsonify(response), 200)


api.register_blueprint(blp)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
  