import logging
import requests
logging.basicConfig(level=logging.ERROR) #added on 18/12/2024

def query_llama3(prompt):
    """
    Queries the Llama3 model using the Ollama API.

    Args:
        prompt (str): The text prompt for Llama3.

    Returns:
        str: The response from Llama3.
    """
    url = "http://localhost:11434/api/chat"  # Default Ollama endpoint
    headers = {"Content-Type": "application/json"}
    payload = {
      "model": "llama3",
      "messages": [{"role": "user", "content": prompt}],
      "stream": False
  }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        if "response" in data:
            return data["response"]
        else:
            return "Unexpected response format from Llama3 API"
        #return response.json().get("response")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error querying Llama3: {e}") # added on 18/12/2024
        return f"Error querying Llama3: {str(e)}"
