import time
import requests
class LLMProvider:
    def __init__(self, base_url="http://localhost:1234/v1", model="llama-3.2-3b-instruct", max_retries=3):
        self.base_url = base_url
        self.model = model
        self.max_retries = max_retries
    def ask(self, question):
        last_error = None
        for attempt in range(self.max_retries):
            try:
                response = requests.post(
                    f"{self.base_url}/chat/completions",
                    json={
                        "model": self.model,
                        "messages": [{"role": "user", "content": question}],
                    },
                    timeout=60,
                )
                response.raise_for_status()
                data = response.json()
                return data["choices"][0]["message"]["content"]
            except requests.exceptions.RequestException as error:
                last_error = error
                wait_time = 2 ** attempt
                print(f"Attempt {attempt + 1} failed ({error}). Retrying in {wait_time}s...")
                time.sleep(wait_time)
        raise RuntimeError(f"Could not reach the model after {self.max_retries} attempts: {last_error}")
