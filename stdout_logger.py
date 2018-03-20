from logger import logger

class stdout_logger:

    """
    Constructor
    """
    def __init__(self, log_level):
        self.__log_level__ = log_level


    """
    log
    """
    def log(self, log_level, message):
        if log_level <= self.__log_level__:
            print(str(log_level) + ": " + message)
