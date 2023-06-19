from config.rule import RuleConfig
from core.sliding_window import SlidingWindow
from limiter.rate_limiter_interface import RateLimiterInterface
import time

config = RuleConfig()


class SlidingWindowLimiter(RateLimiterInterface):
    _instance = None
    rate_limiter = None
    # Can be modified to handle Identifier

    def __new__(cls, identifier):
        cls.rate_limiter = {user_id: SlidingWindow()
                            for user_id in identifier.users}
        return cls

    @classmethod
    def instance(cls, identifier):
        if cls._instance is None:
            cls._instance = cls.__new__(cls, identifier)
        return cls._instance

    @classmethod
    def get_access(cls, key):
        if key not in cls.rate_limiter:
            cls.rate_limiter[key] = SlidingWindow()

        access_obj = cls.rate_limiter[key]
        cur_time = int(time.time())

        if cls._is_allowed(cur_time, access_obj):
            print("Access granted -- Status-200", key)
            access_obj.register(cur_time)   # add a new request
            return True
        print("Access revoked--- Limit Breached -- Status-429", key)
        return False

    @staticmethod
    def _is_allowed(ts, access_obj):
        start_time = ts - access_obj.time
        cur_req = access_obj.get_window_size(start_time)
        print(access_obj.capacity, access_obj.time)
        if cur_req >= access_obj.capacity:
            return False
        return True


class TokenBucketLimiter(RateLimiterInterface):
    def __init__(self):
        pass

    def get_access(self, identifier):
        pass
