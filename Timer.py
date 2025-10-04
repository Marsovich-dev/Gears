import time
class Timer():
    def __init__(self, seconds=0, minutes=0, hours=0):
        self.stop_time = seconds + (minutes // 60) + (hours // 3600)
        self.expire = False

    def start(self):
        self.start_time = time.time()

    def run(self):
        current_time = time.time()
        if (current_time - self.start_time) >= self.stop_time:
            self.expire = True

    def get_expire(self):
        return self.expire
