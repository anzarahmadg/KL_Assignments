import logging

if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()

import os.path
import sys
from configparser import BasicInterpolation, ConfigParser


class EnvInterpolation(BasicInterpolation):
    """
    Interpolation which expands environment variables in values.
    """

    def before_get(self, parser, section, option, value, defaults):
        value = super().before_get(parser, section, option, value, defaults)

        if not os.path.expandvars(value).startswith("$"):
            return os.path.expandvars(value)
        else:
            return


try:
    config = ConfigParser(interpolation=EnvInterpolation())
    config.read("conf/application.conf")
except Exception as e:
    print(f"Error while loading the config: {e}")
    print("Failed to Load Configuration. Exiting!!!")
    sys.stdout.flush()
    sys.exit()


class Service:
    module_name = config["MODULE"]["name"]
    port = config["SERVICE"]["port"]
    host = config["SERVICE"]["host"]
    enable_security = config.getboolean("SERVICE", "enable_security", fallback=True)
    secure_cookie = config.getboolean("SERVICE", "secure_cookie", fallback=True)
    allow_cross_origin = config.getboolean("SERVICE", "allow_cross_origin")
    SELF_PROXY = config["SERVICE"]["proxy"]
    logging_level = config["SERVICE"]["log_level"]
    protected_hosts = os.environ.get("PROTECTED_HOSTS", "").split(",")
    verify_signature = config.getboolean("SERVICE", "verify_signature")
    # Other iLens Services:
    META_SERVICE_URL = config["PATH_TO_OTHER_SERVICES"]["meta_service"]


class DBConf:
    MONGO_URI = config.get("MONGO_DB", "uri")
    if not MONGO_URI:
        print("Error, environment variable MONGO_URI not set")
        sys.exit(1)


class RedisConfig:
    uri = config.get("REDIS", "uri")
    login_db = config.getint("REDIS", "login_db")
    project_tags_db = config.getint("REDIS", "project_tags_db")
    user_role_permissions = config.getint("REDIS", "user_role_permissions")


class MQTTConf:
    uri = config["MQTT"]["uri"]
    host = config["MQTT"]["host"]
    port = int(config["MQTT"]["port"])
    publish_base_topic = config["MQTT"]["publish_base_topic"]


class PathToStorage:
    BASE_PATH = config.get("DIRECTORY", "base_path")
    if not BASE_PATH:
        print("Error, environment variable BASE_PATH not set")
        sys.exit(1)
    MOUNT_DIR = config.get("DIRECTORY", "mount_dir")
    if not MOUNT_DIR:
        print("Error, environment variable MOUNT_DIR not set")
        sys.exit(1)
    MODULE_PATH = os.path.join(BASE_PATH, MOUNT_DIR)
    IMAGES_PATH = os.path.join(MODULE_PATH, "images/")
    LOG_PATH = os.path.join(BASE_PATH, "logs", MOUNT_DIR)


class KeyPath:
    keys_path = config["DIRECTORY"]["keys_path"]
    public = os.path.join(PathToStorage.BASE_PATH, keys_path, "public")
    private = os.path.join(PathToStorage.BASE_PATH, keys_path, "private")
    if not os.path.isfile(public) or not os.path.isfile(private):
        logging.warning("Login Token Keys are not available! Authentication may fail!")
