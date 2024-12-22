from database import fetch_latest_url
from scraper import scrape_website
from classifier import classify_content

if __name__ == "__main__":
    url = fetch_latest_url()
    limited_text_content = scrape_website(url)
    print(limited_text_content)
    classification = classify_content(limited_text_content)
    print(classification)