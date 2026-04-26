# AI Snort Alert Triage System

A real-time SOC-style project that detects network attacks using Snort and analyzes alerts using Python and AI.

## Workflow
Attack → Snort → Alert Log → Triage → AI Analysis → Report

## Features
- Custom SYN scan detection rule
- Real-time alert monitoring
- Severity classification (Low / Medium / High)
- AI-generated explanation and response suggestions
- JSON and Markdown report output

## Tech Stack
- Python
- Snort
- Nmap
- Google Gemini API

## Run
```bash
sudo snort -i lo -A fast -c /etc/snort/snort.conf
sudo ../venv/bin/python main.py
nmap -sS 127.0.0.1
nmap -sS 172.20.20.10
