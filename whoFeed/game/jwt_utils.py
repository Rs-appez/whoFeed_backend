from cryptography.hazmat.primitives import serialization
import jwt
from django.conf import settings


def make_jwt(content):
    private_key = serialization.load_ssh_private_key(
        settings.SECRET_JWT_KEY.encode(), password=b""
    )
    return jwt.encode(
        content,
        private_key,
        algorithm="RS256",
    )


def decode_jwt(token):
    try:
        private_key = serialization.load_ssh_private_key(
            settings.SECRET_JWT_KEY.encode(), password=b""
        )
        public_key = private_key.public_key()
        return jwt.decode(token, public_key, algorithms="RS256")
    except jwt.ExpiredSignatureError:
        return {"error": "Token expired"}

    except jwt.InvalidTokenError:
        return {"error": "Invalid token"}

    except jwt.InvalidSignatureError:
        return {"error": "Invalid signature"}

    except Exception as e:
        return {"error": e}
