from parser import Parser
from geoloc import Geoloc


class Dasher(object):
    """
    Dasher class definition.

    Simply the middleware between the raw datalog and the view functions.
    Takes the raw lists of usefull info and does all the counting and preparing
    for view by Flask.
    """

    def __init__(self, config):
        """
        Inits the object by registering the configuration object
        """
        self.config = config
        self.parser = Parser(self.config)
        self.geoloc = Geoloc(self.config)

        self.data = self.parser.getData()

    def initialCheck(self):
        """
        Once the class is instanciated, this method will do the basic checks
        from the logs and call different other functions.
        """
        bans = []

        for entry in self.data:
            ban = {}
            # Step 1 : get the geoloc data corresponding to the IP address
            geoloc = self.geoloc.get(entry["ip"])
