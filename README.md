<a href="https://crawlbase.com/signup?utm_source=github&utm_medium=readme&utm_campaign=crawling_api_banner" target="_blank">
  <img src="https://github.com/user-attachments/assets/afa4f6e7-25fb-442c-af2f-b4ddcfd62ab2" 
       alt="crawling-api-cta" 
       style="max-width: 100%; border: 0;">
</a>

# 🛒 Scrape Gumtree Data Easily with Python

A complete Python scraper to extract product listings and individual product details from [Gumtree](https://www.gumtree.com), including support for pagination and data export to CSV. Optionally, integrate with [Crawlbase Smart Proxy](https://crawlbase.com) to bypass rate limits and IP bans.

📖 Read the full tutorial → [How to Scrape Gumtree Data Easily](https://crawlbase.com/blog/scrape-gumtree-data-easily/)

## 📌 Features

- Scrape Gumtree **search listings** (title, price, location, URL)
- Scrape **individual product pages** (title, price, description, seller name, image URLs)
- Handle **pagination** across multiple search result pages
- Export data to **CSV** files
- Optional integration with **Crawlbase Smart Proxy** for optimized scraping

---

## 🧰 Requirements

Install Python dependencies:

```bash
pip install requests beautifulsoup4 pandas
```

## 🔍 Gumtree Listings Scraper

**File:** `gumtree_listings_scraper.py`

This script collects product listings from Gumtree's search results and supports multiple pages.

```bash
python gumtree_listings_scraper.py
```

📄 Sample output saved as: `gumtree_listings.csv`

## 📦 Gumtree Product Details Page Scraper

**File:** `gumtree_product_details_scraper.py`

Scrape additional product details like description, seller name, and image URLs:

```bash
python gumtree_product_details_scraper.py
```

📄 Sample output saved as: `gumtree_product_data.csv`

## ⚡️ Boost with Crawlbase Smart Proxy (Optional)

To avoid rate limits, CAPTCHA challenges, or IP bans, you can proxy requests through [Crawlbase Smart Proxy](https://crawlbase.com/smart-proxy):

Example:

```python
proxy_url = "http://_USER_TOKEN_@smartproxy.crawlbase.com:8012"
proxies = {"http": proxy_url, "https": proxy_url}

response = requests.get(url, proxies=proxies, verify=False)
```

🪪 Replace `_USER_TOKEN_` with your Crawlbase token.
