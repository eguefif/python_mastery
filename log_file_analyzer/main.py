from parser import load_logs, load_logs_stream


def main():
    for log in load_logs_stream("./logs/logfiles.log"):
        print(log)
        input()


if __name__ == "__main__":
    main()
