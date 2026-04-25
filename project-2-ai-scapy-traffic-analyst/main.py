from sniffer import start_sniffing
from detector import detect_port_scan
from analyzer import analyze
import json
import time

def save_report(text):
    with open("output/report.md", "w") as f:
        f.write(text)

def save_alert(alerts):
    with open("alerts/alerts.json", "w") as f:
        json.dump(alerts, f, indent=4)

print("Starting live monitoring...")

while True:
    print("\nCapturing traffic...")

    packets = start_sniffing(10)

    alerts = detect_port_scan(packets)

    if alerts:
        print("⚠️ Suspicious activity detected!")

        analysis = analyze(str(alerts))

        print(analysis)

        save_report(analysis)
        save_alert(alerts)

    else:
        print("No suspicious activity.")

    time.sleep(5)
