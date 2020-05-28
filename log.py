import coloredlogs
import logging



LOG_LEVEL = "DEBUG"

class Logger():
    """ Colored logging object based on *coloredlogs* library """
    def __init__(self, object):
        self.logger = logging.getLogger(object.__class__.__name__)
        coloredlogs.install(level=LOG_LEVEL, logger=self.logger)
        self.debug = self.logger.debug
        self.info = self.logger.info
        self.warning = self.logger.warning
        self.error = self.logger.error
        self.critical = self.logger.critical
