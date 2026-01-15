from itertools import tee

from analyzer import analyze_response_sizes, group_by_ip
from parser import load_logs_stream


def main():
    entries = load_logs_stream("./logs/logfiles.log")
    entries1, entries2 = tee(entries)
    stats = analyze_response_sizes(entries1)
    print(stats)
    ips = group_by_ip(entries2)
    print(len(ips))


if __name__ == "__main__":
    main()
