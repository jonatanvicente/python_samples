import requests
from bs4 import BeautifulSoup

# Base URL of the website to scrape
base_url = 'http://books.toscrape.com/catalogue/category/books'

# Number of pages to scrape
num_pages = 5

for page in range(1, num_pages + 1):
    # Construct the URL for the current page
    url = f'{base_url}{page}'

    # Send a GET request to the website
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all article titles (assuming they are in <h2> tags)
        titles = soup.find_all('h2')

        # Print the titles
        print(f'Page {page} titles:')
        for title in titles:
            print(title.get_text())
        print('-' * 40)
    else:
        print(f"Failed to retrieve page {page}. Status code: {response.status_code}")