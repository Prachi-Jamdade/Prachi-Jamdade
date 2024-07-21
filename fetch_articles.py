import feedparser
import os

# Function to fetch articles from the RSS feed
def fetch_articles():
    feed_url = "https://medium.com/feed/@Prachi-Jamdade"
    feed = feedparser.parse(feed_url)
    articles = []

    for entry in feed.entries[:10]:
        article = f"- [{entry.title}]({entry.link})"
        articles.append(article)

    return "\n".join(articles)

# Function to update the README.md file
def update_readme(articles):
    readme_path = "README.md"
    with open(readme_path, "r") as file:
        readme_content = file.read()

    start_marker = "<!-- ARTICLES -->"
    end_marker = "<!-- /ARTICLES -->"

    if start_marker not in readme_content:
        print("Placeholder not found in README.md")
        return

    new_content = f"{start_marker}\n\n{articles}\n\n{end_marker}"
    updated_content = readme_content.split(start_marker)[0] + new_content + readme_content.split(end_marker)[1]

    with open(readme_path, "w") as file:
        file.write(updated_content)

if __name__ == "__main__":
    articles = fetch_articles()
    update_readme(articles)
