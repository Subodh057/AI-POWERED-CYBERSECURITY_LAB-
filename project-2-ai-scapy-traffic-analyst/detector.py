from collections import defaultdict

def detect_port_scan(packets):
    ip_ports = defaultdict(set)

    for pkt in packets:
        try:
            src = pkt["IP"].src

            if pkt.haslayer("TCP"):
                port = pkt["TCP"].dport
                ip_ports[src].add(port)

        except:
            continue

    alerts = []

    for ip, ports in ip_ports.items():
        if len(ports) > 10:
            alerts.append({
                "type": "Port Scan",
                "source_ip": ip,
                "ports_scanned": list(ports)
            })

    return alerts
