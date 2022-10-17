#TODO: make an abstract class
class Module:
    """
    Abstract Module
    """
    _headers = {}
    def __init__(self, headers: dict = {}):
        self._headers.update(headers)
    
    def setTarget(self, host: str, path: str, https: bool = True):
        self._https = https
        self._host = host
        self._path = path
