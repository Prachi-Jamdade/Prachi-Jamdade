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

def update_readme():
    with open('recent_articles.md', 'r') as ra:
        recent_articles = ra.read()

    with open('README.md', 'r') as readme:
        readme_content = readme.read()

    start_marker = '<!-- START_SECTION:recent_articles -->'
    end_marker = '<!-- END_SECTION:recent_articles -->'

    start_idx = readme_content.find(start_marker) + len(start_marker)
    end_idx = readme_content.find(end_marker)

    updated_content = (readme_content[:start_idx] + "\n" + 
                       recent_articles + "\n" + 
                       readme_content[end_idx:])

    with open('README.md', 'w') as readme:
        readme.write(updated_content)

if __name__ == "__main__":
    FEED_URL = 'https://medium.com/feed/@Prachi-Jamdade'
    feed_content = fetch_articles(FEED_URL)
    articles = parse_articles(feed_content)
    write_article_names('recent_articles.md', articles)
    update_readme()
