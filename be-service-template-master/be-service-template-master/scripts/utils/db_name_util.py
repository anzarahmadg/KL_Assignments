import json
from functools import lru_cache


@lru_cache()
def get_db_name(redis_client, project_id: str, database: str, delimiter="__"):
    if not project_id:
        return database
    val = redis_client.get(project_id)
    if val is None:
        raise ValueError(f"Unknown Project, Project ID: {project_id} Not Found!!!")
    val = json.loads(val)
    if not val:
        return database

    # Get the prefix flag to apply project_id prefix to any db
    prefix_condition = bool(val.get("source_meta", {}).get("add_prefix_to_database"))

    if prefix_condition:
        # Get the prefix name from mongo or default to project_id
        prefix_name = val.get("source_meta", {}).get("prefix") or project_id
        return f"{prefix_name}{delimiter}{database}"
    return database


@lru_cache()
def get_redis_db_prefix(redis_client, project_id: str, delimiter="__"):
    if not project_id:
        return False
    val = redis_client.get(project_id)
    if val is None:
        return False
    val = json.loads(val)
    if not val:
        return False

    # Get the prefix flag to apply project_id prefix to any db
    prefix_condition = bool(val.get("source_meta", {}).get("add_prefix_to_database"))

    if prefix_condition:
        # Get the prefix name from mongo or default to project_id
        prefix_name = val.get("source_meta", {}).get("prefix") or project_id
        return f"{prefix_name}{delimiter}"
    return False
