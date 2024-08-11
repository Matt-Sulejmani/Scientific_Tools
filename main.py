# System imports
import atexit
import json
import logging.config
import logging.handlers
import pathlib


# Module imports
import tkinter as Tk

# Package imports
from modules import *


logger = logging.getLogger(__name__)

def setup_logger() -> None:
    """
    This function setsup the logger for the project. It loads the config.json
    file and sets up the logger based on that.
    """
    config_file = pathlib.Path("./config.json")

    with open(config_file) as file:
        config = json.load(file)
    
    logging.config.dictConfig(config)
    queue_handler = logging.getHandlerByName("queue_handler")
    if queue_handler is not None:
        queue_handler.listener.start()
        atexit.register(queue_handler.listener.stop)



## Program entry point
if __name__ == "__main__":
    ...