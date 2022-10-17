#TODO: make an abstract class
class Module:
    """
    Abstract Module
    """
    headers = {}
    def __init__(self, headers: dict = {}):
        self.headers.update(headers)
    
    def setTarget(self, host: str, path: str, https: bool = True):
        self.https = https
        self.host = host
        self.path = path
