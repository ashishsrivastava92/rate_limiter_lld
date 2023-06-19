from rate_limiter_lld.indentifier.identifier_interface import Identifier

class User:
    def __init__(self, user_id: int, meta: dict) -> None:
        self.user_id = user_id
        self.meta = meta

    def get_user(self):
        return self.user_id


class UserIdentifier(Identifier):
    def __init__(self) -> None:
        self.users = set()

    def get_user_identifier(self, user_id):
        if user_id in self.users:
            return user_id
        raise KeyError("User id doesn't exist")

    def get(self):
        return self.users

    def add_identifier(self, user) -> None:
        self.users.add(user.user_id)

# Possible can be other type of identifiers - eg - IP etc


class IdentifierFactory:

    @staticmethod
    def build_identifier(identifier_type: str) -> Identifier:
        if identifier_type == "User":
            identifier = UserIdentifier()
            return identifier
        else:
            raise ValueError("Incorrect identifier type")
