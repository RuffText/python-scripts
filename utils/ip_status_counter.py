def log_analyzer(raw_logs):
    ip_counts = {}
    status_counts = {}
    for log in raw_logs:
        ip, status = log.split(' - ')
        ip_counts[ip] = ip_counts.get(ip, 0) + 1
        status_counts[ip] = status_counts.get(status, 0) + 1

if __name__ == "__main__":
    raw_logs = [
        "192.168.1.5 - 200",
        "10.0.0.12 - 404",
        "192.168.1.5 - 200",
        "192.168.1.5 - 500",
        "10.0.0.12 - 404",
        "172.16.0.4 - 200",
        "192.168.1.5 - 200",
    ]
    log_analyzer(raw_logs)