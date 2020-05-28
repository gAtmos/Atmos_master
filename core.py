# Libraries
import time
from datetime import datetime

# Utilities
from log import Logger


class Core():
    """ Orchestrator object. Can read configuration file to plan actions """

    DATE_FORMAT = "%Y-%m-%d %H:%M"
    WAIT_INTERVAL = 1

    def __init__(self, config="config.json"):
        # Create a logger object.
        self.logger = Logger(self)
        self.logger.info("starting core")

    @staticmethod
    def parse_date(date_str: str):
        """ Parse a date from a string """
        date = datetime.strptime(date_str, format=Core.DATE_FORMAT)
        self.logger.debug(f"parsing date {date_str} to datetime object {date}")
        return date
        

    @staticmethod
    def date_to_str(date: datetime):
        date_str = date.strftime(Core.DATE_FORMAT)
        self.logger.debug(f"putting date {date} to string {date_str}")
        return date_str

    
    def wait_next_tick(self, interval=WAIT_INTERVAL):
        """ Waits for the next tick with the given interval between ticks """
        time_to_wait = interval - (time.time() % interval)
        self.logger.debug(f"waiting {time_to_wait}ms before next tick")
        time.sleep(time_to_wait)


    def mainloop(self):
        """ Starts the mainloop that processes idle tasks and waits the necessary time before the next tick """
        self.logger.debug("starting main loop")
        while True:
            # Wait for next tick
            self.wait_next_tick()


if __name__ == "__main__":
    # Tests
    config_path = "./test_config.json"
    
    c = Core(config=config_path)
    c.mainloop()
    