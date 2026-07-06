import pytest
import requests
from unittest.mock import patch, Mock
from agent.llm import LLMProvider
def test_ask_returns_answer_on_success():
    provider = LLMProvider()
    fake_response = Mock()
    fake_response.json.return_value = {"choices": [{"message": {"content": "Test answer"}}]}
    with patch("agent.llm.requests.post", return_value=fake_response) as mock_post:
        answer = provider.ask("What is testing?")
    assert answer == "Test answer"
    mock_post.assert_called_once()
def test_ask_raises_after_max_retries():
    provider = LLMProvider(max_retries=2)
    with patch("agent.llm.requests.post", side_effect=requests.exceptions.ConnectionError("boom")):
        with patch("agent.llm.time.sleep"):
            with pytest.raises(RuntimeError):
                provider.ask("Will this fail?")
