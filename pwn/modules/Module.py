import urllib.parse
#TODO: make an abstract class
class Module:
    """
    Abstract Module
    """
    _defaultRequestType = "get"
    _headers = {}
    _https = True
    _host = ""
    _path = "/"
    _defaultGetVars = {}
    _defaultPostVars = {}

    def __init__(self, headers: dict = {}):
        self._headers.update(headers)
    
    def setTarget(self, host: str, path: str, getVariables: dict = {}, postVariables: dict = {}, https: bool = True, forcePost: bool = False):
        self._https = https
        self._host = host
        self._path = path

        self._defaultGetVars = getVariables.copy()
        sel._defaultPostVars = postVariables.copy()
        if forcePost or len(postVariables) > 0:
            self._defaultRequestType = "post"

    def buildURI(self, withDefaultGetParams: bool = True, forceDisableURLEncoding: bool = False) -> str:
        """
            Build Target URI
            This method builds the standard target URI
            
            :param bool withDefaultGetParams: appends the default get params on the URI
            :param bool forceDisableURLEncoding: forcefully disables url encoding for get params (might be dangerous)
            :return: the built url
            :rtype: str
        """
        url = "http{}://".format("s"*self._https)
        url += self._host
        url += self._path
        # get params
        if withDefaultGetParams and len(self._defaultGetVars) > 0:
            # escape weird stuff through url encoding
            url += "?"
            for param in self._defaultGetVars.items():
                url += param[0]
                url += "="
                if forceDisableURLEncoding:
                    url += param[1]
                else:
                    url += urllib.parse.quote(param[1])
                url += "&"
            url.removesuffix("&")
        return url
