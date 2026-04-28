🛡️ Incident Analysis Report (SOC)

1. What attack is happening?

The source IP 172.20.10.10 is performing a vertical and horizontal port scan.

* Probing multiple ports including well-known (21, 22, 80, 443) and high ephemeral ports
* Behavior matches reconnaissance activity to identify exposed services

⸻

2. Why it is dangerous?

* Pre-attack reconnaissance phase
* Helps attacker identify vulnerable services
* Enables targeted exploitation and lateral movement
* Indicates potential compromised internal host or insider activity

⸻

3. Risk Level: HIGH

* Aggressive scanning pattern across wide port range
* Internal IP involvement increases risk
* Strong indicator of malicious intent

⸻

4. Recommended Actions

1. Isolate host 172.20.10.10 immediately
2. Identify asset owner and system role
3. Review EDR logs for suspicious processes
4. Check outbound traffic for C2 communication
5. Investigate user activity linked to the host
6. Harden and patch scanned target systems

⸻

5. MITRE ATT&CK Mapping

* Tactic: Reconnaissance (TA0043)
* Technique: Network Service Discovery (T1046)

Explanation:
The activity aligns with MITRE ATT&CK T1046, where attackers scan network services to identify open ports and running applications as part of the reconnaissance phase.

⸻

🔍 Summary

This is a Priority 1 reconnaissance incident.
The behavior strongly suggests active network enumeration, requiring immediate containment and investigation.