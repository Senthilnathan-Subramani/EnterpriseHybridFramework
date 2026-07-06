from loguru import logger
from .paths import LOGS
LOGS.mkdir(exist_ok=True)
logger.add(LOGS/'framework.log', rotation='10 MB')
get_logger=lambda: logger
