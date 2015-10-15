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
            self.log = open(config.log_file)

    def isLog(line):
        """
        Checks if a log entry is a fail2ban log entry
        """
        # TODO : Change this to some regex magic ?
        if "fail2ban" in line and "Ban" in line:
            return True
        else:
            return False

    def parseAll(self):
        """
        Parses all the previous entries in the fail2ban log without realtime
        support.
        """
        entries = []
        while True:
            line = self.log.readline()
            if self.isLog(line):
                entries.append(line)

        return entries

    def parseRT(self):
        """
        Parses the log file in realtime : only the upcoming log bans will be
        """
        # TODO : maybe use a separate thread for rt parsing ?
        pass
