from logger import logger

class file_logger:

    """
    Constructor
    """
    def __init__(self, log_level):
        self.__log_level__ = log_level
        self._file_= open('file_log.txt', 'a+')


    """
    log
    """
    def log(self, log_level, message):
        if log_level <= self.__log_level__:
            self._file_.write(str(log_level) + ': ' + message + '\n')
