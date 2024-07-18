import redis

from config import REDIS_USER, REDIS_USER_PASSWORD

r = redis.Redis(
    host="redis",
    port=6379,
    db=0,
    username=REDIS_USER,
    password=REDIS_USER_PASSWORD,
)
