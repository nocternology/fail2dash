class Parser(object):
    """
    Parser class definition.

    Takes care of parsing the fail2ban log, either in "all" mode or "realtime".
    """

    def __init__(self, config, mode=None):
        """
        Inits the object by registering the configuration object
        """
        self.config = config
        if mode is None:
            self.mode = config.parse_default

    def parseAll(self):
        """
        Parses all the previous entries in the fail2ban log without realtime
        support.
        """
