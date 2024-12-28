import requests
import ollama

def generate_query(text_input, model="codellama"):
    url = 'http://localhost:11434/v1/completions'
    headers = {
        'Content-Type': 'application/json',
    }

    prompt = f"""You are sql DML query generator for PostgreSQL. This is table you can operate on: 
        create table url
       (
       id              bigint not null
         constraint url_pkey1
              primary key,
      long_url        varchar(255),
      short_url       varchar(255),
      expiration_date timestamp(6),
      url_open_count  bigint,
      category        varchar(255)
    );
    Generate query based on the following input: {text_input}
    Here's a SQL DML statement to insert a new row into the `url` table:..
    I want only query no additional text
    """
    payload ={
        "model": model,
        "prompt": prompt
    }

    response = requests.post(url, headers=headers, json=payload)
    #check if there is response
    if response.status_code == 200:
        query = response.json()['choices'][0]['text']
        return query
    return "No response from the model"

def generate_query_1(text_input, model="llama3.2:3b"):
    response = ollama.chat(
        model = model,
        messages=[
            {"role": "system", "content": f"You are sql DML query generator for PostgreSQL. This is table you can operate on: create table url ( id bigint not null constraint url_pkey1 primary key, long_url varchar(255), short_url varchar(255), expiration_date timestamp(6), url_open_count bigint, category varchar(255) );"},
            {"role": "user", "content": f"Generate query based on the following input: {text_input}"},
            {"role": "system", "content": "Here's a SQL DML statement to insert a new row into the `url` table:.."},
            {"role": "user", "content": "I want only query, no additional text"}
        ]
    )
    return response['message']['content']