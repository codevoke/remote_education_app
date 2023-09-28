"""creating api from all namespace to build it in app.py"""
from flask_restx import Api

# from .filename import namespace_name


api = Api(
    title="Remote education server API",
    version="1.0",
    description="API provided access to authorize system and other private methods"
)

# api.add_namespace(namespace_name)
