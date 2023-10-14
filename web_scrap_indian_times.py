from bs4 import BeautifulSoup
import requests

# Specify the URL of the website you want to fetch
url = "https://indianexpress.com/"  # Replace with the URL of the website you want to fetch

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200 indicates success)
if response.status_code == 200:
    # Get the HTML content from the response
    html_content = response.text


    # Now, you can work with the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    title = soup.title
    print(f"Title of the page: {title.text}")
    
     # Find all <figure> tags in the HTML
    figure_tags = soup.find_all('figure')

    # Extract and print the link and content text from each <figure> tag
    for figure in figure_tags:
        # Find the <a> tag within the <figure> tag
        a_tag = figure.find('a')
        img_tag = figure.find('img')

        if img_tag:
            # Extract and print the image source (src attribute) within the <img> tag
            image_src = img_tag.get('src')
            print("Image Source:", image_src)
        
        if a_tag:
            # Extract and print the link (href attribute) within the <a> tag
            link = a_tag.get('href')
            print("Link:", link)

        # Find and print the text content within the <figure> tag
        content_text = figure.get_text()
        if (content_text == ''):
            content_text = a_tag.get('title')
        
        print("Content Text:", content_text)
        print('\n\n\n')
else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")
