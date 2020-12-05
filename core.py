# Libraries
import time
import json
from datetime import datetime

# Utilities
from log import Logger


logging = Logger() # TODO Change to Leo's logging script

class Core():
    """ Orchestrator object. Can read configuration file to plan actions """

    DATE_FORMAT = "%Y-%m-%d %H:%M"
    WAIT_INTERVAL = 60 * 60 * 24

    def __init__(self, initial_config="config.json"):
        
        # Create a logger object.
        logging.info("starting core")

        if initial_config:
            self.parse_config(initial_config)

    @staticmethod
    def parse_date(date_str: str):
        """ Parse a date from a string """
        date = datetime.strptime(date_str, format=Core.DATE_FORMAT)
        logging.debug(f"parsing date {date_str} to datetime object {date}")
        return date
        

    @staticmethod
    def date_to_str(date: datetime):
        date_str = date.strftime(Core.DATE_FORMAT)
        logging.debug(f"putting date {date} to string {date_str}")
        return date_str

    
    def wait_next_tick(self, interval=WAIT_INTERVAL):
        """ Waits for the next tick with the given interval between ticks """
        time_to_wait = interval - (time.time() % interval)
        logging.debug(f"waiting {time_to_wait}ms before next tick")
        time.sleep(time_to_wait)


    def parse_config(self, config_path):
        try:
            config = json.load(open(config_path))
        except FileNotFoundError as fnf_error:
            logging.error(f"Config file {config_path} not found.")
            return
        
        

    def mainloop(self):
        """ Starts the mainloop that processes idle tasks and waits the necessary time before the next tick """
        logging.debug("starting main loop")
        while True:
            # Wait for next tick
            self.wait_next_tick()


if __name__ == "__main__":
    # Tests
    config_path = "./test_config.json"
    
    c = Core(initial_config=config_path)
    c.mainloop()
    