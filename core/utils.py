import socket
import os


def getHostname():
    """
    Returns the current host hostname
    """
    return socket.gethostname()


def fail2banStatus():
    """
    Returns the status of fail2ban for init and systemd
    """
    f = os.popen('service fail2ban status')
    status = f.read()
    if ("inactive" in status or "not running" in status):
        return False
    elif ("active" in status or "is running" in status):
        return True


def gatherHostInfo():
    """
    Tidy up the host information in a nice list for template rendering
    """
    info = {}
    info['active'] = fail2banStatus()
    info['hostname'] = getHostname()

    return info
