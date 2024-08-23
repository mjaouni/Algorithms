# The goal is to keep track of the number of unique IP addresses
# that visit the website in the last 10 minutes at any given point in time.

from collections import deque
from datetime import datetime, timedelta

import time


class WebsiteTrafficMonitor:  # Time complexity O(n)
    def __init__(self):
        self.visitors = deque()
        self.unique_ips = set()
        self.window_size = timedelta(minutes=10)

    def add_visit(self, ip):
        current_time = datetime.now()

        # Remove visits outside the 10-minute window
        while self.visitors and self.visitors[0][1] < current_time - self.window_size:
            old_ip, old_timestamp = self.visitors.popleft()
            if old_ip not in (ip for ip, in self.visitors):
                self.unique_ips.remove(old_ip)

        # Add new visit to the queue and set
        self.visitors.append((ip, current_time))
        self.unique_ips.add(ip)

    def get_unique_visitor_count(self):
        return len(self.unique_ips)


# Usage
monitor = WebsiteTrafficMonitor()

monitor.add_visit('192.168.1.1')
monitor.add_visit('192.168.1.2')
monitor.add_visit('192.168.1.3')

time.sleep(300)  # Sleep for 5 minutes to simulate time passage

monitor.add_visit('192.168.1.1')
monitor.add_visit('192.168.1.4')

# Get the number of unique visitors in the last 10 minutes
print(f"Unique visitor count: {monitor.get_unique_visitor_count()}")
