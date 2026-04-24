As a SOC Analyst, I have analyzed the provided logs. Here is the incident report:

### 1. Summary
The logs indicate a series of repeated **Brute Force and Credential Stuffing attacks** against the host `subodh-awasthi-Vostro-3500`. The activity is observed across three distinct timeframes, involving two different external source IPs and one local loopback address. The attacker is systematically attempting to authenticate using a wide dictionary of common usernames (e.g., `admin`, `root`, `MGR`, `manager`, `operator`).

### 2. Attack Type
*   **Brute Force / Password Spraying:** Attempting multiple password combinations or testing a large list of usernames to gain unauthorized access via SSH.

### 3. MITRE Techniques
*   **T1110.001 (Brute Force: Password Guessing):** Systematically attempting to guess passwords.
*   **T1110.003 (Brute Force: Password Spraying):** Using a common password list or a dictionary of usernames to gain access.
*   **T1078.004 (Valid Accounts: Cloud Accounts/SSH):** Attempting to authenticate via SSH using guessed credentials.

### 4. Risk Level
**High**
*   **Reasoning:** While there is no evidence of a *successful* login (only "Failed password" entries), the high volume of attempts and the diverse range of attempted usernames suggest automated malicious activity. The targeting of `root` and `admin` accounts indicates an intent to achieve privilege escalation upon entry.

### 5. Indicators (IOCs)
*   **Attacker Source IPs:**
    *   `192.168.1.71` (Primary source for dictionary-style attacks)
    *   `192.168.1.82` (Source for targeted attacks on `subodh-awasthi` user)
    *   `127.0.0.1` (Self-referential, likely an local misconfiguration or an attacker who has already gained local shell access on the machine).
*   **Patterns:**
    *   Rapid, sequential SSH login failures within seconds of each other.
    *   Use of common default/administrative usernames: `admin`, `root`, `MGR`, `MANAGER`, `OPERATOR`, `sysadm`, `supervisor`.
    *   High-frequency authentication attempts originating from local/private IP ranges.

### 6. Recommended Response
1.  **Immediate Containment:** 
    *   Block IPs `192.168.1.71` and `192.168.1.82` at the network firewall immediately.
    *   Investigate the `127.0.0.1` activity; if the machine is a server, check for local malicious processes or compromised web shells that might be initiating these local SSH attempts.
2.  **Hardening:**
    *   Disable SSH password authentication and enforce **SSH Key-based authentication** only.
    *   Disable remote root login in `/etc/ssh/sshd_config` (`PermitRootLogin no`).
    *   Implement **Fail2Ban** to automatically ban IPs that exceed a threshold of failed login attempts.
3.  **Audit:**
    *   Review all successful SSH logins for the dates `2026-04-14`, `2026-04-17`, and `2026-04-24` to ensure no accounts were compromised during periods where brute force was active.
    *   Rotate passwords for all users identified in the attack logs (e.g., `subodh-awasthi`).
4.  **Monitoring:** 
    *   Set up a real-time alert in Splunk for `Failed password` events exceeding 5 attempts in a 1-minute window per source IP.