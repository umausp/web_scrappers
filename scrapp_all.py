import requests
from bs4 import BeautifulSoup

# List of news websites to scrape
news_websites = [
    {
        "name": "CNN",
        "url": "https://edition.cnn.com/world",
    },
    {
        "name": "BBC",
        "url": "https://www.bbc.com/news/world",
    },
    # Add more websites as needed
]

# Function to scrape and display news from a website
def scrape_and_display_news(website):
    print(f"--- {website['name']} News ---")
    response = requests.get(website['url'])
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        # Modify this section to extract headlines and article URLs based on the website's structure
        # Here, we are simply printing the first 5 headlines and URLs.
        news_articles = soup.find_all("div", class_="container__headline container_lead-plus-headlines__headline")
        for i, article in enumerate(news_articles, start=1):
            article_url = article.get("href")
            article_title = article.text
            print(f"{i}. {article_title}")
            print(f"   URL: {article_url}")
            print()

    else:
        print(f"Failed to retrieve {website['name']} news. Status code: {response.status_code}")
    print("\n")

# Iterate through the list of news websites and scrape news
for website in news_websites:
    scrape_and_display_news(website)
