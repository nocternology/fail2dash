import urllib
import json


class Geoloc(object):
    """
    Geoloc class definition.

    Given an IP adress, this object will try to reverse identify the IP using
    a geolocalisation API.

    On the return, it will spit back a list with :
    * IP adress,
    * Longitude,
    * Latitude,
    * Country,
    * Country flag
    """

    def __init__(self, config):
        """
        Inits the object by registering the configuration object
        """
        self.config = config

    def get(self, ip):
        """
        Metamethod that returns the full geoloc information for a given IP adress
        """
        geoloc["ip"] = ip
        return geoloc

    def getLocationAPI(self, ip):
        """
        Makes the actual call to the external API for IP geolookup
        """
        try:
            response = urllib.urlopen(config.api_endpoint % ip)
            info = response.read()
        except Exception as e:
            # TODO : Add some kind of logging here

        if config.api_parser == "json":
            # Just in case you use an XML API or whatever
            result = self.parseJSON(info)

        # TODO : Get country flag from a local CSS/SVG
        # (see : https://github.com/lipis/flag-icon-css)

    def parseJSON(self, info):
        """
        Gets a JSON message and parse it to keep only the relevant parts for us
        """
        parsed = json.loads(info)

        return {'lat': parsed['latitude'], 'lon': parsed['longitude'],
                'country': parsed['country'], 'code': parsed['country_code3']}
