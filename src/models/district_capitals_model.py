import mongoengine as mongo


class Capital(mongo.Document):
    # meta = {"collection_alias": "capital"}
    COV_DIST_1 = mongo.IntField(required=True)
    NAMECAP = mongo.StringField(required=True)
    DISTRICT = mongo.StringField(required=True)
    POPCAP = mongo.IntField(required=True)
    POINT_X = mongo.FloatField(required=True)
    POINT_Y = mongo.FloatField(required=True)
    xcoord = mongo.FloatField(required=True)
    ycoord = mongo.FloatField(required=True)
