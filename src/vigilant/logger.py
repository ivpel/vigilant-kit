import logging
import os

logging.basicConfig(format='[%(asctime)s: %(levelname)s] %(message)s')

logger = logging.getLogger(__name__)
logger.setLevel(os.environ.get("LOGGER_LEVEL", "INFO"))
