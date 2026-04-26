import time
import json
from parser import parse_alerts
from triage import triage_alerts
from analyzer import analyze

last_alert_count = 0

def save(alerts, report):
    with open("alerts/alerts.json", "w") as f:
        json.dump(alerts, f, indent=4)

    with open("output/report.md", "w") as f:
        f.write(report)

print("🚀 Monitoring Snort alerts...")

while True:
    alerts = parse_alerts()

    if len(alerts) > last_alert_count:
        print("\n⚠️ New alert detected!\n")

        
        latest_alert = alerts[-1:]  # only last alert
        triaged = triage_alerts(latest_alert)
        result = analyze(str(triaged))

        print(result)

        save(triaged, result)

        last_alert_count = len(alerts)

    time.sleep(5)
