import json

import paho.mqtt.client as mqtt

from scripts.config import MQTTConf
from scripts.logging import logger


def on_connect(rc):
    logger.debug("Publisher Connected with result code " + str(rc))


def push_notification(notification, user_id):
    try:
        client = mqtt.Client()
        client.on_connect = on_connect
        client.connect(MQTTConf.host, MQTTConf.port, 30)
        topic = f"{MQTTConf.publish_base_topic}/{user_id}/reports"
        client.publish(topic, json.dumps(notification), retain=False, qos=1)
        logger.info(f"Notification message published to {topic}")
        logger.debug(f"Notification: {notification}")
        client.disconnect()
        return True
    except Exception as e:
        logger.exception(f"Exception at MQTT Publish: {e}")
        return False
