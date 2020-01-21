# -*- coding: utf-8 -*-
"""Helper Module for Carson Living tests."""
import os
import time
import jwt

from tests.const import TOKEN_PAYLOAD_TEMPLATE


def load_fixture(folder, filename):
    """Load a fixture."""
    path = os.path.join(os.path.dirname(__file__),
                        'fixtures', folder, filename)
    with open(path) as fdp:
        return fdp.read()


def get_encoded_token(expiration_from_now_s=600):
    """Generate a standard Carson Living Token with variable expiration

    Args:
        expiration_from_now_s: delta in s to the current_time

    Returns:
        (tuple): tuple containing:

            token(str): encoded token
            token_payload(dict): decoded token payload
    """
    token_payload = {'exp': int(time.time() + expiration_from_now_s)}
    token_payload.update(TOKEN_PAYLOAD_TEMPLATE)

    token = jwt.encode(token_payload, 'secret', algorithm='HS256')

    return token, token_payload
