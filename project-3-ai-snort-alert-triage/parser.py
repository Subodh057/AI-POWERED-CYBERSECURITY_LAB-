def parse_alerts(file_path="/var/log/snort/alert"):
    alerts = []

    try:
        with open(file_path, "r") as f:
            lines = f.readlines()

        for line in lines:
            if "->" in line:
                parts = line.strip().split()
                src = parts[-3]
                dst = parts[-1]

                alerts.append({
                    "source_ip": src,
                    "destination_ip": dst,
                    "raw": line.strip()
                })

    except Exception as e:
        print("Error reading alerts:", e)

    return alerts
