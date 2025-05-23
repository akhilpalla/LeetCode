class Logger:

    def __init__(self):
        self.rate_limited_messages = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.rate_limited_messages:
            rate_limit_timestamp = self.rate_limited_messages[message]
            if timestamp < rate_limit_timestamp:
                return False
        self.rate_limited_messages[message] = timestamp + 10
        return True

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)