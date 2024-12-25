from database import fetch_latest_url, fetch_all_urls
from scraper import scrape_website
from classifier import classify_content

if __name__ == "__main__":
    #url = fetch_latest_url()
    urls = fetch_all_urls()
    print(urls)
    # for url in urls:
    #  limited_text_content = scrape_website(url)
    #  classification = classify_content(limited_text_content)
    #  print(classification + " - " + url)
    # url ="https://www.google.com"
    # limited_text_content = scrape_website(url)
    # classification = classify_content(limited_text_content)
    # print(classification + " - " + url)