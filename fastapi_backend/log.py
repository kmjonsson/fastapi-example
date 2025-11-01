import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s: %(message)s"
)

log = logging.getLogger("fast-api-backend")
log.setLevel(logging.DEBUG)
