def triage_alerts(alerts):
    results = []

    for alert in alerts:
        severity = "Low"
        raw = alert["raw"].lower()

        if "scan" in raw:
            severity = "Medium"

        if "syn" in raw or "port scan" in raw:
            severity = "High"

        alert["severity"] = severity
        results.append(alert)

    return results
