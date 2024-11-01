import requests
from bs4 import BeautifulSoup
import random
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# URL of the Amazon product page
url = "https://www.amazon.com/s?k=laptop"

# Get page content
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Find product titles and prices
products = soup.find_all('div', {'data-component-type': 's-search-result'})
for product in products:
    title = product.h2.text.strip()
    price = product.find('span', 'a-price')
    if price:
        price = price.find('span', 'a-offscreen').text
    else:
        price = "Price not available"
    
    print(f"Title: {title}")
    print(f"Price: {price}")
    print("-" * 20)

    # Sleep to avoid getting blocked
    time.sleep(random.uniform(1, 3))

print({title})