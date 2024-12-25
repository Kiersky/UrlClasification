import requests

def classify_content(text_content, model="llama3.2:3b"):
    """Classify the content using the local Ollama instance."""
    url = 'http://localhost:11434/v1/completions'
    headers = {
        'Content-Type': 'application/json',
    }
    prompt = text_content + "classify what category of website is it, return category in 1 word only"
    payload = {
        "prompt": prompt,
        "model": model
    }
    # response = requests.post(url, headers=headers, json=payload)
    # if response.status_code == 200:
    #     data = response.json()
    #     return data['choices'][0]['text']
    # else:
    #     raise Exception(f"Request failed with status code {response.status_code}")
    i=0
    response = requests.post(url, headers=headers, json=payload)
    while response.status_code == 200 and i<10:
        i+=1
        print(i)
        data = response.json()
        print(data['choices'][0]['text'])
        if len(data['choices'][0]['text'].split()) == 1 :
            return data['choices'][0]['text']
        response = requests.post(url, headers=headers, json=payload)
    return "unclassified"
