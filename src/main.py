from database import *
from scraper import scrape_website
from classifier import classify_content
from query_generator import generate_query
if __name__ == "__main__":
    #url = fetch_latest_url()
    # fetched_urls = fetch_all_urls()
    # url_list = [list(fetched_urls) for fetched_urls in fetched_urls]
    # url_list = [item[:2] for item in url_list]
    # print(url_list)

    # for url in url_list:
    #     limited_text_content = scrape_website(url[1])
    #     url.append(classify_content(limited_text_content))
    #     print(str(url[0]) + " - " + url[1] + " - " + url[2])
    # print(url_list)
    #updating categories in database
    # for record in url_list:
    #     update_category(record)

    query = generate_query("remove record with id 1 ", model="llama3.2:3b")
    print(query)
    execute_query(query)