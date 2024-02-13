import json


class User:
    def __init__(self, user_id: int, name: str, friends: list[int]):
        self.user_id: int = user_id
        self.name: str = name
        self.friends: list[int] = friends

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)