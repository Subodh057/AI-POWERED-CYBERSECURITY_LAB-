PROMPT = """
You are a SOC analyst.

Analyze this detected network behavior:

{log_data}

Explain:
1. What attack is happening
2. Why it is dangerous
3. Risk level
4. What action should be taken.
5. MITRE ATT&CK mapping (tactic + technique).

"""
