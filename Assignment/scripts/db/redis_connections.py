import redis

from scripts.config import RedisConfig

redis_uri = RedisConfig.uri

login_db = redis.from_url(
    redis_uri, db=int(RedisConfig.login_db), decode_responses=True
)

project_details_db = redis.from_url(
    redis_uri, db=int(RedisConfig.project_tags_db), decode_responses=True
)

user_role_permissions_redis = redis.from_url(
    redis_uri, db=int(RedisConfig.user_role_permissions), decode_responses=True
)
