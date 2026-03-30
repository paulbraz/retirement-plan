from utility.logging_helper import configure_logging
from pathlib import Path

configure_logging(Path(__file__).parent.parent.parent / "logging_config.yaml")
