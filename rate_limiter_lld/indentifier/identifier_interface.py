from abc import ABC, abstractmethod


class Identifier(ABC):

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def get_user_identifier(self, user_id):
        pass

    @abstractmethod
    def add_identifier(self, key):
        pass