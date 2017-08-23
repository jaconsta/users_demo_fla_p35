from flask import Flask
from flask_cors import CORS
import mongoengine

# Url Setings
API_PREFIX = '/api/v1'

app = Flask(__name__)
CORS(app)

# Database connection
MONGO_URI = "mongodb://localhost:32768/lavanda"
mongoengine.connect(host=MONGO_URI)

# Application threads.
THREADS_PER_PAGE = 2

# CRSF.
CSRF_ENABLED = False
CSRF_SESSION_KEY = "ASecretKey"


from app.users.views import UserApiListView, UserApiView, LoginApiView

# Register routes
app.add_url_rule(API_PREFIX+'/user/<string:id>', view_func=UserApiView.as_view('user'))
app.add_url_rule(API_PREFIX+'/user', view_func=UserApiListView.as_view('user_list'))
app.add_url_rule(API_PREFIX+'/login', view_func=LoginApiView.as_view('user_login'))


if __name__ == '__main__':
    app.run()
