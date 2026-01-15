from array import array
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
