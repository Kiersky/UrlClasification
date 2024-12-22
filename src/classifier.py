import requests

def classify_content(text_content):
    """Classify the content using the local Ollama instance."""
    url = 'http://localhost:11434/v1/completions'
    headers = {
        'Content-Type': 'application/json',
    }
    prompt = text_content + "classify in only one word what type of content is on this website, return only one word"
    payload = {
        "prompt": prompt,
        "model": "llama3.1:latest"
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        return data['choices'][0]['text']
    else:
        raise Exception(f"Request failed with status code {response.status_code}")