# Configuration class for Fail2Dash


class Config():
    # Basic configuration about the application
    debug = True

    # Authentication configuration
    auth_mail = "root@localhost"
    auth_password = "test"
    secret = "8897879668D998AD5E9C4200E90E6056BBEB2FA38745ECA4D6710BC535ACDA02"

    # Fail2Ban parsing configuration
    log_file = ""

    # Geolocalisation API setup
    api_endpoint = "https://www.telize.com/geoip/%s"
    api_parser = "json"
