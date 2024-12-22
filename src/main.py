import psycopg2
import requests
from bs4 import BeautifulSoup

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname='postgres',
    user='postgres',
    password='mysecretpassword',
    host='localhost',
    port='5432'
)
cursor = conn.cursor()

# Execute a query to fetch data
cursor.execute("SELECT long_url FROM url ORDER BY id DESC LIMIT 1")

url_tuple = cursor.fetchone()
url = url_tuple[0]

# Close the connection
conn.close()

# URL of the website
#url = 'https://example.com'

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the text content
text_content = soup.get_text()

limited_text_content = text_content[:100]

#print(text_content)
print(limited_text_content)

# Define the URL of the local Ollama instance
url = 'http://localhost:11434/v1/completions'  # Replace with the actual endpoint

# Define the headers and payload for the request
headers = {
    'Content-Type': 'application/json',
    #'Authorization': 'Bearer YOUR_API_KEY'  # Replace with your actual API key if needed
}

part1 ="classify in only one word what type of content is on this website, return only one word"
prompt = limited_text_content + part1

payload = {
    "prompt": prompt,
    "model": "llama3.1:latest"
}

# Send a POST request to the local Ollama instance
response = requests.post(url, headers=headers, json=payload)

# Check the response status code
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    text_value = data['choices'][0]['text']
    print(text_value)
else:
    print(f"Request failed with status code {response.status_code}")