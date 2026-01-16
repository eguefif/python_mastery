from typing import Generator


def parse_log_line(line: str) -> tuple:
    """
    Parse a line and return tuple with unamed field
         0. client ip           6. Size of the request in bytes
         1. remote logname      7. referer
         2. remote user         8. user agent
         3. timestamp []        9. response time
         4. request line
         5. HTTP code

        Log example:

    12.72.169.173 - - [27/Dec/2037:12:00:00 +0530] "POST /usr/admin/developer HTTP/1.0" 304 4979 "http://peterson-dunn.com/posts/postsfaq.php" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/746A194A" 1453
    """
    tokens = []
    token = ""
    ignore_space = False
    for c in line.strip():
        if c == " " and not ignore_space:
            tokens.append(token)
            token = ""
        elif c in ['"', "[", "]"]:
            ignore_space = not ignore_space
        else:
            token += c

    tokens.append(token)
    return tuple(tokens)


def is_success(code: str) -> bool:
    return int(code) <= 400


def load_logs(filename: str, filter_successful=False) -> list[tuple[str, ...]]:
    """
    Read a file and return a list that provides Tupple

    filter_successful: returns http query with code lesser than 400
    stream: if True return an iterator
    """
    with open(filename, "r") as f:
        if filter_successful:
            return [
                parse_log_line(line) for line in f.readlines() if is_success(line[5])
            ]

        return [parse_log_line(line) for line in f.readlines()]


def load_logs_stream(
    filename: str, filter_successful=False
) -> Generator[tuple[str, ...]]:
    """Read a file and return an iterator that provides Tupple

    filter_successful: returns http query with code lesser than 400
    stream: if True return an iterator

    """
    with open(filename, "r") as f:
        if filter_successful:
            return (
                parse_log_line(line) for line in f.readlines() if is_success(line[5])
            )
        return (parse_log_line(line) for line in f.readlines())
