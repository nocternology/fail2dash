#!/usr/bin/python

from parser import Parser
import utils
from geoloc import Geoloc

# Default config for testing purposes


class Config():
    # Basic configuration about the application
    debug = True

    # Authentication configuration
    auth_mail = "root@localhost"
    auth_password = "test"
    secret = "8897879668D998AD5E9C4200E90E6056BBEB2FA38745ECA4D6710BC535ACDA02"

    # Fail2Ban parsing configuration
    log_file = "/home/nocternology/Work/fail2dash/sample.log"
    parse_default = "all"

    # Geolocalisation API setup
    api_endpoint = "https://www.telize.com/geoip/%s"
    api_parser = "json"

config = Config()

# Parser module testing
parser = Parser(config)
data = parser.getData()
# print data
#
# # Host info testing
# print utils.gatherHostInfo()

# Geoloc module testing
geoloc = Geoloc(config)
for entry in data:
    print geoloc.get(entry["ip"])
