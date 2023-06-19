import threading
from collections import defaultdict
from config.rule import RuleConfig


class SlidingWindow:
    def __init__(self):
        self.config = self.get_config()
        self.time = self.config.time * 60  # convert into sec
        self.capacity = self.config.capacity  # max requests ot serve
        self.log = defaultdict()
        self.lock = threading.Lock()

    @staticmethod
    def get_config():
        return RuleConfig()

    def get_window_size(self, start_time):
        # return request count in that window
        req_count = 0
        to_delete = []
        for ts, count in self.log.items():
            if ts > start_time:
                req_count += count
            else:
                to_delete.append(ts)
        for key in to_delete:
            del self.log[key]
        return req_count

    def register(self, ts):
        self.lock.acquire()
        if ts not in self.log:
            self.log[ts] = 1
        else:
            self.log[ts] += 1
        self.lock.release()

