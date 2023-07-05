class ValueNotFound(Exception):
    def __init__(self):
        super().__init__("Value not Found")


class InvalidReactionError(Exception):
    def __init__(self):
        self.value = "The reaction described cannot occur!"