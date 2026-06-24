# Historical events database module
import json
from pathlib import Path


class EventDatabase:

    def __init__(self):

        file = Path(
            "events.json"
        )

        if file.exists():

            with open(
                file,
                encoding="utf8"
            ) as f:

                self.data = json.load(f)

        else:

            self.data = {}

    def find(self, dt):

        key = dt.strftime(
            "%d-%m"
        )

        return self.data.get(
            key,
            []
        )