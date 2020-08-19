import time
import logbook


class Benchmark():
    def __init__(self):
        self.time_wall_start = time.time()
        self.time_cpu_start = time.process_time()
        self.logger = logbook.Logger(self.__class__.__name__)

    def diff_time_wall_secs(self):
        return time.time() - self.time_wall_start

    def print_time(self, label=''):
        self.logger.info(f"{label} wall={self.diff_time_wall_secs() / 60.0:.3f}m "
                         f"cpu={(time.process_time() - self.time_cpu_start) / 60.0:.3f}m" )
