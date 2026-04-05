import requests

PQS_BASE = "https://pqs.onchainintel.net"

try:
    import httpx
    _HTTPX_AVAILABLE = True
except ImportError:
    _HTTPX_AVAILABLE = False


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


class AsyncPQSClient:
    def __init__(self, api_key: str = None):
        if not _HTTPX_AVAILABLE:
            raise ImportError("httpx is required for async support. Run: pip install pqs-sdk[async]")
        self.api_key = api_key
        self.base = PQS_BASE

    async def score(self, prompt: str, vertical: str = "general") -> dict:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base}/api/score/free",
                json={"prompt": prompt, "vertical": vertical},
            )
            response.raise_for_status()
            return response.json()

    async def optimize(self, prompt: str, vertical: str = "general") -> dict:
        if not self.api_key:
            raise ValueError("api_key required for optimize. Get one at pqs.onchainintel.net")
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base}/api/score/full",
                headers={"X-API-Key": self.api_key},
                json={"prompt": prompt, "vertical": vertical},
            )
            response.raise_for_status()
            return response.json()

    async def compare(self, prompt: str, vertical: str = "general") -> dict:
        if not self.api_key:
            raise ValueError("api_key required for compare. Get one at pqs.onchainintel.net")
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base}/api/score/compare",
                headers={"X-API-Key": self.api_key},
                json={"prompt": prompt, "vertical": vertical},
            )
            response.raise_for_status()
            return response.json()


# Sync convenience functions
def score_prompt(prompt: str, vertical: str = "general") -> dict:
    return PQSClient().score(prompt, vertical)

def optimize_prompt(prompt: str, api_key: str, vertical: str = "general") -> dict:
    return PQSClient(api_key=api_key).optimize(prompt, vertical)

def compare_models(prompt: str, api_key: str, vertical: str = "general") -> dict:
    return PQSClient(api_key=api_key).compare(prompt, vertical)


# Async convenience functions
async def async_score_prompt(prompt: str, vertical: str = "general") -> dict:
    return await AsyncPQSClient().score(prompt, vertical)

async def async_optimize_prompt(prompt: str, api_key: str, vertical: str = "general") -> dict:
    return await AsyncPQSClient(api_key=api_key).optimize(prompt, vertical)

async def async_compare_models(prompt: str, api_key: str, vertical: str = "general") -> dict:
    return await AsyncPQSClient(api_key=api_key).compare(prompt, vertical)
