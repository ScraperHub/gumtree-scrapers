import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_gumtree_search(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    listings = []

    for listing in soup.select('article[data-q="search-result"]'):
        title = listing.select_one('div[data-q="tile-title"]').text.strip()
        price = listing.select_one('div[data-testid="price"]').text.strip()
        location = listing.select_one('div[data-q="tile-location"]').text.strip()
        link = listing.select_one('a[data-q="search-result-anchor"]')['href']
        listings.append({
            'title': title,
            'price': price,
            'location': location,
            'URL': f'https://www.gumtree.com{link}'
        })

    return listings

def scrape_gumtree_multiple_pages(base_url, max_pages):
    all_listings = []

    for page in range(1, max_pages + 1):
        url = f'{base_url}?page={page}'
        listings = scrape_gumtree_search(url)
        all_listings.extend(listings)

    return all_listings

def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

def main():
    base_url = 'https://www.gumtree.com/search?q=headset'
    max_pages = 5
    listings = scrape_gumtree_multiple_pages(base_url, max_pages)
    save_to_csv(listings, 'gumtree_listings.csv')
    print(f'Scraped {len(listings)} listings and saved to gumtree_listings.csv')

if __name__ == '__main__':
    main()