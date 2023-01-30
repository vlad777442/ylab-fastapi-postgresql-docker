import json
from fastapi.encoders import jsonable_encoder
from .cache_settings import redis_client


def is_cached(url):
    return redis_client.exists(url)

def get_cache(url):
    value = redis_client.get(url)
    return json.loads(value) if value else value

def set_cache(url, value):
    redis_client.set(url, json.dumps(jsonable_encoder(value)))

def delete_cache(url):
    keys = redis_client.keys(f'{url}*')
    if keys:
        redis_client.delete(*keys)