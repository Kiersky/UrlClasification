import requests
import ollama

category_list = ["Personal or Individual", "Portfolio", "Personal blogs", "Resumes or CVs", "Business and Commercial", "E-commerce", "Corporate", "Service-based", "Educational", "Online learning platforms", "School or university", "Research", "Media and Entertainment", "News", "Streaming", "Music and video", "Community and Social", "Social networks", "Forums or discussion boards", "Nonprofit", "Technology", "Tech blogs", "Software tools", "Gaming", "Health and Fitness", "Healthcare", "Wellness blogs", "Fitness tracking", "Travel and Tourism", "Travel blogs", "Tour operators", "Hotels and accommodation", "Lifestyle", "Food and cooking blogs", "Fashion and beauty", "DIY or crafts", "Professional or Industrial", "Legal", "Construction and real estate", "Financial", "Miscellaneous", "Events", "Q&A, knowledge-sharing", "Auctions"]


def classify_content(text_content, model="llama3.2:3b"):
    """Classify the content using the local Ollama instance."""
    url = 'http://localhost:11434/v1/completions'
    headers = {
        'Content-Type': 'application/json',
    }

    #category_list = ["Personal or Individual", "Portfolio", "Personal blogs", "Resumes or CVs", "Business and Commercial", "E-commerce", "Corporate", "Service-based", "Educational", "Online learning platforms", "School or university", "Research", "Media and Entertainment", "News", "Streaming", "Music and video", "Community and Social", "Social networks", "Forums or discussion boards", "Nonprofit", "Technology", "Tech blogs", "Software tools", "Gaming", "Health and Fitness", "Healthcare", "Wellness blogs", "Fitness tracking", "Travel and Tourism", "Travel blogs", "Tour operators", "Hotels and accommodation", "Lifestyle", "Food and cooking blogs", "Fashion and beauty", "DIY or crafts", "Professional or Industrial", "Legal", "Construction and real estate", "Financial", "Miscellaneous", "Events", "Q&A, knowledge-sharing", "Auctions"]
    payload = {
        "model": model,
        "prompt": f"""You are a classifier model for websites, which returns only category. Category list is: {category_list} or any other you find appropriate.

    What is the category of this website? {text_content}
    This looks like a website about:...
    I want a Response only with the category.
        """

    }
    # TODO consider chat style api

    i=0
    response = requests.post(url, headers=headers, json=payload)
    print(response.json())
    while response.status_code == 200 and i<10:
        i+= 1
        print(i)
        data = response.json()
        print(data['choices'][0]['text'])
        if len(data['choices'][0]['text'].split()) < 4 :
            return data['choices'][0]['text']
        response = requests.post(url, headers=headers, json=payload)
    return "unclassified"

def classify_content_1(text_content, model="llama3.2:3b"):
    res = ollama.chat(
        model=model,
        messages=[
                 {"role": "system", "content": f"You are a classifier model for websites, which returns only category. Category list is: {category_list} or any other you find appropriate."},
                 {"role": "user", "content": f"What is the category of this website? {text_content}"},
                 {"role": "system", "content": "This looks like a website about:..."},
                 {"role": "user", "content": "I want a Response only with the category"}
        ]
    )
    if len(res['message']['content'].split()) < 4:
        return res['message']['content']
    return "unclassified"