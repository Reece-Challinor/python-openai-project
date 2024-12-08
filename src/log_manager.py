import logging
import logging.handlers
import yaml
import os

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

log_level = config["logging"].get("level", "INFO")
log_file = config["logging"].get("file", "logs/app.log")
max_bytes = config["logging"].get("max_bytes", 10485760)
backup_count = config["logging"].get("backup_count", 5)

os.makedirs(os.path.dirname(log_file), exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(getattr(logging, log_level))

handler = logging.handlers.RotatingFileHandler(
    log_file, maxBytes=max_bytes, backupCount=backup_count
)
formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

# Also log to stdout
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

logger.propagate = False
