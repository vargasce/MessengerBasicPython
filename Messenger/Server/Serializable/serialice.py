from json import JSONEncoder
import json

class Serialice(JSONEncoder):
    def default(self, o):
        return o.__dict__
