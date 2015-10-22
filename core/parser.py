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

    def getData(self):
        """
        Generic interface to simply get the logs.
        """

        return self.parseAll()

    def parseAll(self):
        """
        Parses all the previous entries in the fail2ban log without realtime
        support.
        """
        entries = []
        while True:
            line = self.log.readline()
            if line == '':
                break
            if self.isLog(line):
                entries.append(self.tidyLog(line))

        return entries

    def isLog(self, line):
        """
        Checks if a log entry is a fail2ban log entry
        """
        # TODO : Change this to some regex magic ?
        if "fail2ban" in line and "Ban" in line:
            return True
        else:
            return False

    def tidyLog(self, entry):
        """
        Tidies up a single log entry to separate usefull infos.
        """
        # TODO : replace this with some regex magic again
        logLine = {}
        logLine["date"] = entry[0:10]
        logLine["time"] = entry[11:19]
        logLine["service"] = entry[entry.find("[") + 1: entry.find("]")]
        logLine["ip"] = entry[entry.find("Ban") + 4: len(entry) - 1]

        return logLine

    def parseRT(self):
        """
        Parses the log file in realtime : only the upcoming log bans will be
        """
        # TODO : maybe use a separate thread for rt parsing ?
        pass
