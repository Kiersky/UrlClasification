import psycopg2

def fetch_latest_url():
    """Fetch the latest URL from the database."""
    conn = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='mysecretpassword',
        host='localhost',
        port='5432'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT long_url FROM url ORDER BY id DESC LIMIT 1")
    url_tuple = cursor.fetchone()
    conn.close()
    return url_tuple[0]

def fetch_all_urls():
    """Fetch all URLs from the database."""
    conn = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='mysecretpassword',
        host='localhost',
        port='5432'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT long_url FROM url")
    url_tuples = cursor.fetchall()
    conn.close()
    return [url_tuple[0] for url_tuple in url_tuples]