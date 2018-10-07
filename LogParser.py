from json import dumps

def log_parser(filename: str, event_id: int) -> dict:
    """
    Microsoft DHCP Service Activity Log parser
    """
    # Checking varible types
    if not isinstance(filename, str):
        raise TypeError(str(type(filename)) + " is not str")
    if not isinstance(event_id, int):
        raise TypeError(str(type(event_id)) + " is not int")
    elif event_id < 0:
        raise ValueError("event_id must be >= 0")

    count = 0
    users = set()
    for line in open(filename, "r"):
        # splitting string by ','
        # works faster than regular expressions in this case
        arr = line.split(",")
        if arr[0] == str(event_id):
            users.add(arr[4])
            count += 1
    return {
        "event_id": event_id,
        "count": count,
        "users": list(sorted(users))
    }

if __name__ == "__main__":
    res = log_parser("DhcpSrvLog-Thu.log", 11)
    print(dumps(res, indent=4))