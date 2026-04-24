from splunk_api import fetch_splunk_results
from analyzer import analyze
import json


def save_report(text):
    with open("output/report.md", "w") as f:
        f.write(text)


def classify_priority(text):
    if "High" in text or "HIGH" in text:
        return "HIGH"
    elif "Medium" in text or "MEDIUM" in text:
        return "MEDIUM"
    else:
        return "LOW"


def save_alert(text):
    alert = {
        "priority": classify_priority(text),
        "details": text
    }

    with open("alerts/alerts.json", "w") as f:
        json.dump(alert, f, indent=4)


results = fetch_splunk_results()
log_data = json.dumps(results, indent=2)

analysis = analyze(log_data)

print(analysis)

save_report(analysis)
save_alert(analysis)
