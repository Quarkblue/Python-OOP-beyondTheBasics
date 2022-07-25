# Logging
# Python beyond the basics - object oriented programming

"""
Writes logging "events" to file or the terminal screen
Messages are written and logged at levels of "severity":
    DEBUG(debug()): diagnostic messages for development
    INFO(info()): standard "progress" messages
    WARNING(warning()): detected a non-serious issue
    ERROR(error()): detected a serious issue
    CRITICAL(critical()): detected a fatal error
"""


import logging

logging.basicConfig(level=logging.INFO)

logging.debug('this message will be ignored')
logging.info('this should be logged')
logging.warning('this will be logged too')