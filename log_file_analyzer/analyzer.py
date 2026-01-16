from array import array
from collections import deque
from datetime import datetime
from statistics import mean, median, quantiles
from typing import Iterator


def analyze_response_sizes(log_entries: Iterator) -> dict:
    result = {}
    sizes = array("L", [int(row[6]) for row in log_entries])

    result["median"] = median(sizes)
    result["mean"] = mean(sizes)
    result["deciles"] = quantiles(sizes, n=10)

    return result


def group_by_ip(log_entries: Iterator) -> dict:
    """
    Group requests by IP address
    """
    ips = {}
    for entry in log_entries:
        request = (entry[3], entry[4], entry[5])
        if entry[0] in ips.keys():
            ips[entry[0]].append(request)
        else:
            ips[entry[0]] = [request]

    return ips


class TrafficMonitor:
    """
    Track requests per minute using a sliding window
    """

    format = "%d/%b/%Y:%H:%M:%S %z"

    def __init__(self, window_minutes: int = 1):
        self.window_minutes: float = float(window_minutes)
        self.window: deque = deque()

    def add_request(self, timestamp: str):
        """Add a new request timestamp to the window."""
        date = datetime.strptime(timestamp, TrafficMonitor.format).timestamp()
        self.window.append(date)
        self._cleanup_old_requests(date)

    def _cleanup_old_requests(self, current_time: float):
        """Remove timestamps older than our window."""
        while len(self.window) > 0 and (
            (current_time - self.window[0]) > self.window_minutes * 60
        ):
            self.window.popleft()

    def get_current_rate(self, current_time=None) -> float:
        """
        Calculate requests per minute in the current window.

        Args:
            current_time: Time to measure from (defaults to now)

        Returns:
            float: Average requests per minute

        Hint: After cleanup, just divide total requests by window size
        """
        if not current_time:
            current_time = datetime.now().timestamp()

        self._cleanup_old_requests(current_time)
        return len(self.window) / (self.window_minutes * 60)
