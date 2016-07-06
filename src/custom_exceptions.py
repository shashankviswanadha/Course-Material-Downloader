class LoginError(Exception):
    str = None

    def __init__(self, str):
        self.str = str

    def __str__(self):
        return repr(self.str)

class SemesterError(Exception):
    str = None

    def __init__(self, str):
        self.str = str

    def __str__(self):
        return repr(self.str)

class FileError(Exception):
    str = None

    def __init__(self, str):
        self.str = str

    def __str__(self):
        return repr(self.str)

class DownloadError(Exception):
    str = None

    def __init__(self, str):
        self.str = str

    def __str__(self):
        return repr(self.str)

class CourseNameError(Exception):
    str = None

    def __init__(self, str):
        self.str = str

    def __str__(self):
        return repr(self.str)
