from flask import Flask

application = Flask(__name__)
from application.views import simple_page
application.register_blueprint(simple_page)