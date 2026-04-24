import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()

SPLUNK_HOST = "https://localhost:8089"
SPLUNK_USER = os.getenv("SPLUNK_USER")
SPLUNK_PASSWORD = os.getenv("SPLUNK_PASSWORD")


def fetch_splunk_results():
    search_query = 'search index=main "Failed password" | table _time host source _raw'

    create_job_url = f"{SPLUNK_HOST}/services/search/jobs"

    response = requests.post(
        create_job_url,
        auth=(SPLUNK_USER, SPLUNK_PASSWORD),
        data={
            "search": search_query,
            "output_mode": "json"
        },
        verify=False
    )

    response.raise_for_status()
    sid = response.json()["sid"]

    while True:
        status_url = f"{SPLUNK_HOST}/services/search/jobs/{sid}"
        status = requests.get(
            status_url,
            auth=(SPLUNK_USER, SPLUNK_PASSWORD),
            params={"output_mode": "json"},
            verify=False
        )
        status.raise_for_status()

        is_done = status.json()["entry"][0]["content"]["isDone"]

        if is_done:
            break

        time.sleep(1)

    results_url = f"{SPLUNK_HOST}/services/search/jobs/{sid}/results"

    results = requests.get(
        results_url,
        auth=(SPLUNK_USER, SPLUNK_PASSWORD),
        params={
            "output_mode": "json",
            "count": 100
        },
        verify=False
    )

    results.raise_for_status()
    return results.json()["results"]
