import requests
import xml.etree.ElementTree as ET

# URL of the RSS feed
RSS_URL = 'https://medium.com/feed/@Prachi-Jamdade'

# Function to fetch and parse RSS feed
def fetch_articles():
    response = requests.get(RSS_URL)
    response.raise_for_status()  # Check if the request was successful

    # Parse the RSS feed
    root = ET.fromstring(response.content)
    items = root.findall('.//item')

    articles = []
    for item in items:
        title = item.find('title').text
        link = item.find('link').text
        articles.append(f'- [{title}]({link})')

    return '\n'.join(articles)

# Function to update README.md
def update_readme(articles):
    readme_path = 'README.md'
    with open(readme_path, 'r') as file:
        content = file.read()

    # Find the section to update
    start_marker = '<!-- ARTICLES -->'
    end_marker = '<!-- /ARTICLES -->'
    start_index = content.find(start_marker)
    end_index = content.find(end_marker, start_index + len(start_marker))

    if start_index != -1 and end_index != -1:
        before = content[:start_index + len(start_marker)]
        after = content[end_index:]
        new_content = f'{before}\n{articles}\n{after}'
    else:
        new_content = f'{content}\n\n{start_marker}\n\n{articles}\n{end_marker}'

    with open(readme_path, 'w') as file:
        file.write(new_content)

if __name__ == "__main__":
    articles = fetch_articles()
    update_readme(articles)
