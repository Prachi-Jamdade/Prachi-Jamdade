import requests
import xml.etree.ElementTree as ET

def fetch_articles(feed_url):
    response = requests.get(feed_url)
    response.raise_for_status()
    return response.content

def parse_articles(feed_content):
    root = ET.fromstring(feed_content)
    articles = []
    for item in root.findall('./channel/item'):
        title = item.find('title').text
        link = item.find('link').text
        articles.append({'title': title, 'link': link})
    return articles

def write_article_names(file_path, articles):
    with open(file_path, 'w') as f:
        f.write('## Recent Articles\n\n')
        for article in articles:
            f.write(f"- [{article['title']}]({article['link']})\n")

if __name__ == "__main__":
    FEED_URL = 'https://medium.com/feed/@Prachi-Jamdade'
    feed_content = fetch_articles(FEED_URL)
    articles = parse_articles(feed_content)
    write_article_names('recent_articles.md', articles)
