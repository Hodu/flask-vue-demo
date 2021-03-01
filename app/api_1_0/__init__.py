from flask import Blueprint

bp = Blueprint("api_1_0", __name__)

import app.api_1_0.controller
