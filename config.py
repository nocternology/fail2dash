# Configuration class for Fail2Dash


class Config():
    # Basic configuration about the application
    debug = True

    # Authentication configuration
    auth_mail = "root@localhost"
    auth_password = "ee26b0dd4af7e749aa1a8ee3c10ae9923f618980772e473f8819a5d4940e0db27ac185f8a0e1d5f84f88bc887fd67b143732c304cc5fa9ad8e6f57f50028a8ff"  # AKA test
    secret = "8897879668D998AD5E9C4200E90E6056BBEB2FA38745ECA4D6710BC535ACDA02"

    # Fail2Ban parsing configuration
    log_file = ""
    parse_default = "rt"

    # Geolocalisation API setup
    api_endpoint = "https://www.telize.com/geoip/%s"
    api_parser = "json"
