from limiter.rate_limiter import SlidingWindowLimiter
from indentifier.user_identification import User, IdentifierFactory


class RateLimiterDriver:

    def create_identifier(self, identifier_type):
        return IdentifierFactory.build_identifier(identifier_type)

    def __init__(self, identifier_type):        # Algorithm
        self.identifier = self.create_identifier(identifier_type)  # sets self.identifier
        self.sliding_limiter = SlidingWindowLimiter.instance(self.identifier)
        # self.ip_sliding_limiter = SlidingWindowLimiter.instance(self.identifier)
        self.users = dict()

    def create_user(self, user_id, meta=dict()):
        user = User(user_id, meta)
        self.users[user_id] = user
        self.identifier.add_identifier(user)

    def handle(self, user_id):
        self.sliding_limiter.get_access(user_id)


if __name__ == "__main__":
    import time
    driver = RateLimiterDriver("User")
    driver.create_user(123, {"name": "Ashish"})
    print(driver.users)
    for i in range(14):
        time.sleep(4)
        driver.handle(123)
        if i > 9:
            time.sleep(5)
    driver.create_user(234, {"name": "Abhinav"})
    for i in range(10):
        driver.handle(234)

