"""Utilites for work with jwt separatly"""
import os
from time import time as current_time

from flask_restx import reqparse
import jwt


def jwt_validator(token: str) -> dict | ValueError:
    """
    validate token value and return payload or raise Exceptions optional

    :token: jwt token from Headers by key 'Authorization'
    """
    try:
        auth_type, token_value = token.split(" ")
        if auth_type != "Bearer":
            raise ValueError("Authorization type must be Bearer")
    except ValueError as exc:
        raise ValueError("Token must have '<auth_type> <token_value>' format") from exc
    try:
        payload = jwt.decode(
            token_value,
            os.getenv("APP_SECRET_KEY"),
            algorithms=["HS256"]
        )
        return payload
    except jwt.ExpiredSignatureError as exc:
        raise ValueError("Token has expired") from exc
    except jwt.InvalidTokenError as exc:
        raise ValueError("Token is invalid") from exc


jwt_required = reqparse.RequestParser()
jwt_required.add_argument(
    "Authorization",
    type=jwt_validator,
    required=True,
    help="Method is private! Access denied.",
    location="headers"
)


WEEK_IN_SECONDS = 60 * 60 * 24 * 7


def generate_token(
        payload: dict,
        time: int =current_time() + WEEK_IN_SECONDS,
        secret_key: str =os.getenv("APP_SECRET_KEY")
        ) -> str:
    """
    generate jwt token 

    :payload:     payload for encoding into token
    :time:        time in seconds of token expire time
    :secret_key:  key for token secure
    """
    payload['exp'] = time

    jwt_token = jwt.encode(
        payload=payload,
        key=secret_key,
        algorithm="HS256",
    )
    return jwt_token