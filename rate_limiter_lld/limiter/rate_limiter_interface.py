from abc import ABC, abstractmethod


class RateLimiterInterface(ABC):

    @abstractmethod
    def get_access(self, identifier):
        pass
