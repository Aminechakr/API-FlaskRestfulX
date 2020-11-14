from flask import Flask
from flask_restx import Ressource, Api

app = Flask("__name__")
api = Api(app)

@api.route("/hello")
class HelloWorld(Ressource):
    def get(self):
        return {"hello message": "Hi from Flask RestfulX"}

    @api.route("/home")
    class HelloWorld(Ressource):
        def get(self):
            return {"Welcome message: You are at your flask restX Api, you can start adding great other methods and functions"}


if __name__ == "__main__":
    app.run(debug=True)
#    app.run