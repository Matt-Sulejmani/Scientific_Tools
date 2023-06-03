class ValueNotFound(Exception):
    def __init__(self):
        super().__init__("Value not Found")