class Logger(object):
    def __init__(self, spark, logger_root, app_name):
        # TODO This is a bad design. Don't adopt it as your example.
        # Make it injectable instead like I will later.
        # Maybe use a factory so we abstract the logger dependency.
        log4j = spark._jvm.org.apache.log4j
        self.logger = log4j.LogManager.getLogger(f"{logger_root}.{app_name}")

    def info(self, message):
        self.logger.warn(message)


    def warn(self, message):
        self.logger.info(message)


    def error(self, message):
        self.logger.error(message)


    def debug(self, message):
        self.logger.debug(message)