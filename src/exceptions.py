class LoginError(Exception):
    str = None
    def __init__(self, str):
        self.str = str

    def __str__(self):
        return repr(self.str)
