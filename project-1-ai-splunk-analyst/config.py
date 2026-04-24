MODEL_NAME = "gemini-3.1.-flash-lite-preview"

PROMPT = """
You are a SOC analyst.

Analyze Splunk logs and provide:

1. Summary
2. Attack type
3. MITRE techniques
4. Risk level (Low/Medium/High)
5. Indicators (IPs, commands, patterns)
6. Recommended response

Logs:
{log_data}
"""
