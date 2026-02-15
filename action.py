import os
import hmac
import json
import hashlib
import datetime

import urllib.request


B12_URL = "https://b12.io/apply/submission"
SHA256_SIGNING_SECRET = os.getenv("SHA256_SIGNING_SECRET")
GITHUB_SERVER_URL = os.getenv("GITHUB_SERVER_URL")
GITHUB_REPOSITORY = os.getenv("GITHUB_REPOSITORY")
GITHUB_RUN_ID = os.getenv("GITHUB_RUN_ID")


def main():

    data = {
        "action_run_link": f"{GITHUB_SERVER_URL}/{GITHUB_REPOSITORY}/actions/runs/{GITHUB_RUN_ID}",
        "email": "christopher.antonellis@gmail.com",
        "name": "Christopher Antonellis",
        "repository_link": f"{GITHUB_SERVER_URL}/{GITHUB_REPOSITORY}",
        "resume_link": "https://drive.google.com/file/d/1AyxaOHK4_O6KwUruJg3S9N_57-ROF3lp/view?usp=drive_link",
        "timestamp": datetime.now().isoformat()
    }

    data_encoded = json.dumps(data).encode("utf-8")
    signing_secret_encoded = SHA256_SIGNING_SECRET.encode("utf-8")
    hex_digest = hmac.new(signing_secret_encoded, data_encoded, hashlib.sha256).hexdigest()

    headers = {
        "Content-Type": "application/json",
        "X-Signature-256": f"sha256={hex_digest}"
    }

    request = urllib.request.Request(B12_URL, data=data, headers=headers)

    with urllib.request.urlopen(request) as response:
        response_data = response.read().decode("utf-8")
        print(response_data)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        exit(e)