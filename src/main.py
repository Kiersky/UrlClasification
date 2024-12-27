from database import *
from scraper import scrape_website
from classifier import classify_content
from query_generator import generate_query
from flask  import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
#CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

@app.route('/generate_query', methods=['POST'])
def generate_sql_query():
    data = request.json
    text_input = data.get('text_input')
    if not text_input:
        return jsonify({'error': 'No text input provided'}), 400
    query = generate_query(text_input)
    return jsonify({'query': query})
@app.route('/confirm_query', methods=['POST'])
def confirm_query():
    data = request.json
    query = data.get('query')
    if not query:
        return jsonify({'error': 'No query provided'}), 400
    execute_query(query)
    return jsonify({'message': 'Query executed successfully'})
##TODO and query hashing for security
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)



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


    # for record in url_list:
    #     update_category(record)

    # query = generate_query("remove record with id 1 ", model="llama3.2:3b")
    # print(query)
    # execute_query(query)