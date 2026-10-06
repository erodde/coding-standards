import os, sys
from datetime import datetime

SERVERS = [
    {"name": "Webserver", "status": "online", "response_time": 120},
    {"name": "Datenbank", "status": "offline", "response_time": 0},
    {"name": "Backupserver", "status": "online", "response_time": 340},
]


def check_server(server_name, status, response_time=0):
    if status == "online" and response_time < 500:
        return {
            "name": server_name,
            "reachable": True,
            "message": "Server ist erreichbar",
        }
    else:
        return {
            "name": server_name,
            "reachable": False,
            "message": "Server ist nicht erreichbar",
        }


def create_report(servers):
    report = []
    for server in servers:
        result = check_server(server["name"], server["status"], server["response_time"])
        report.append(result)
    return report


def print_report(report):
    print("\nServerbericht")
    print("-------------")
    for result in report:
        state = "OK" if result["reachable"] else "FEHLER"
        print(f"[{state}] {result['name']}: {result['message']}")


if __name__ == "__main__":
    report = create_report(SERVERS)
    print_report(report)
