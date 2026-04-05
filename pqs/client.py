import requests

PQS_BASE = "https://pqs.onchainintel.net"

VERTICALS = ["software", "content", "business", "education", "science", "crypto", "general"]


class PQSClient:
    def __init__(self, api_key: str = None):
        self.api_key = api_key
        self.base = PQS_BASE

    def score(self, prompt: str, vertical: str = "general") -> dict:
        response = requests.post(
            f"{self.base}/api/score/free",
            json={"prompt": prompt, "vertical": vertical},
        )
        response.raise_for_status()
        return response.json()

    def optimize(self, prompt: str, vertical: str = "general") -> dict:
        if not self.api_key:
            raise ValueError("api_key required for optimize. Get one at pqs.onchainintel.net")
        response = requests.post(
            f"{self.base}/api/score/full",
            headers={"X-API-Key": self.api_key},
            json={"prompt": prompt, "vertical": vertical},
        )
        response.raise_for_status()
        return response.json()

    def compare(self, prompt: str, vertical: str = "general") -> dict:
        if not self.api_key:
            raise ValueError("api_key required for compare. Get one at pqs.onchainintel.net")
        response = requests.post(
            f"{self.base}/api/score/compare",
            headers={"X-API-Key": self.api_key},
            json={"prompt": prompt, "vertical": vertical},
        )
        response.raise_for_status()
        return response.json()


def score_prompt(prompt: str, vertical: str = "general") -> dict:
    return PQSClient().score(prompt, vertical)

def optimize_prompt(prompt: str, api_key: str, vertical: str = "general") -> dict:
    return PQSClient(api_key=api_key).optimize(prompt, vertical)

def compare_models(prompt: str, api_key: str, vertical: str = "general") -> dict:
    return PQSClient(api_key=api_key).compare(prompt, vertical)
