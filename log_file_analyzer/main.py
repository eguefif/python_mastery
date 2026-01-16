import random
from itertools import tee
from time import sleep, time

from analyzer import TrafficMonitor, analyze_response_sizes, group_by_ip
from parser import load_logs_stream


def main():
    entries = load_logs_stream("./logs/logfiles.log")
    entries1, entries2, entries3 = tee(entries, 3)
    stats = analyze_response_sizes(entries1)
    print(stats)
    ips = group_by_ip(entries2)
    print(len(ips))

    tracker = TrafficMonitor()
    count = 0
    timer = [0.1]  # , 0.05, 0.08]
    now = time()
    for entry in entries3:
        tracker.add_request(entry[3])
        sleep(random.choice(timer))
        diff = int(time() - now)
        if diff > 50 and diff % 60 == 0:
            print(tracker.get_current_rate())

        count += 1


if __name__ == "__main__":
    main()
