import os
import random
import time
import requests
from bs4 import BeautifulSoup
from celery import shared_task
from .models import Brand, Product 
import logging 

# Set up Django settings for this script
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "amazon_scraper.settings")

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)  # Set logging level to INFO

USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    # Add more user agents for rotation
]

@shared_task(bind=True, max_retries=3)
def scrape_amazon_products(self):
    logger.info("Started scraping Amazon products.")
    
    for brand in Brand.objects.all():
        logger.info(f"Processing brand: {brand.name}")
        try:
            page = 1
            while True:
                url = f"https://www.amazon.com/s?k=apple&page={page}"  # Include the page number in the URL
                headers = {'User-Agent': random.choice(USER_AGENTS)}
                response = requests.get(url, headers=headers)

                logger.info(f"Fetching URL: {url} (Status: {response.status_code})")

                if response.status_code != 200:
                    logger.error(f"Request failed with status {response.status_code} for URL: {url}")
                    raise Exception(f"Request failed with status {response.status_code}")

                soup = BeautifulSoup(response.text, 'html.parser')

                products = soup.select('.s-result-item[data-asin]')
                if not products:
                    logger.info(f"No products found on page {page} for brand {brand.name}.")
                    break

                for item in products:
                    product_name = item.select_one('h2 .a-text-normal').get_text(strip=True) if item.select_one('h2 .a-text-normal') else None
                    asin = item.get('data-asin')
                    image_url = item.select_one('img').get('src') if item.select_one('img') else None
                    sku = asin  # Default SKU to ASIN if not provided

                    if product_name and asin:
                        logger.info(f"Saving product: {product_name} (ASIN: {asin})")
                        Product.objects.update_or_create(
                            asin=asin,
                            defaults={
                                'name': product_name,
                                'image_url': image_url,
                                'sku': sku,
                                'brand': brand
                            }
                        )
                    else:
                        logger.warning(f"Missing product name or ASIN for item: {item}")

                page += 1
                time.sleep(random.uniform(2, 5))

            logger.info(f"Completed scraping for brand: {brand.name}")

        except E
