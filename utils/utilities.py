from json import load
from datetime import datetime


class Utility:

    @staticmethod
    def get_payload(path):
        with (open(path, "r")) as json_file:
            json_data = load(json_file)
            json_data["owTilesParameters"]["pointSet"] = "AUTO_MS_TILE_" + str(int(datetime.timestamp(datetime.now())))
            return json_data
