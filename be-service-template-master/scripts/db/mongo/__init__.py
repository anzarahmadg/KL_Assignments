from pydantic import BaseModel

from scripts.config import DBConf
from scripts.utils.mongo_util import MongoCollectionBaseClass, MongoConnect

mongo_uri = DBConf.MONGO_URI

mongo_obj = MongoConnect(uri=mongo_uri)

mongo_client = mongo_obj()

CollectionBaseClass = MongoCollectionBaseClass


class MongoBaseSchema(BaseModel):
    pass
