from database import fetch_latest_url, fetch_all_urls, update_category
from scraper import scrape_website
from classifier import classify_content

if __name__ == "__main__":
    #url = fetch_latest_url()
    fetched_urls = fetch_all_urls()
    url_list = [list(fetched_urls) for fetched_urls in fetched_urls]
    url_list = [item[:2] for item in url_list]
    print(url_list)

    for url in url_list:
        limited_text_content = scrape_website(url[1])
        url.append(classify_content(limited_text_content))
        print(str(url[0]) + " - " + url[1] + " - " + url[2])
    print(url_list)
    #updating categories in database
    # for record in url_list:
    #     update_category(record)
