import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    """Scrape the website and return the text content."""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text_content = soup.get_text()
    return text_content[:100]