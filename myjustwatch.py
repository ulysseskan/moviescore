"""Retrieve url + whether movie is available on streaming from JustWatch"""
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def search(query):
    """Search JustWatch for a given movie and return streaming services with year, title, and URL"""
    url = f"https://www.justwatch.com/us/search?q={query}"
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.content, 'html.parser')

    div_tags = soup.select_one('div.price-comparison__grid__row--stream')
    if div_tags is not None:
        img_tags = div_tags.select('img.price-comparison__grid__row__icon')
        year_tag = soup.select_one('span.header-year')
        year = year_tag.text.strip("()") if year_tag else ""
        title_tag = soup.select_one('span.header-title')
        title = title_tag.text.strip() if title_tag else ""
        link_tag = soup.select_one('a.title-list-row__column-header')
        url = urljoin("https://www.justwatch.com", link_tag.get('href')) if link_tag else ""

        streaming_services = [img_tag.get('title') for img_tag in img_tags]

        return {
            "title": title,
            "streaming_services": streaming_services,
            "year": year,
            "url": url
        }

    return {
        "title": "",
        "streaming_services": [],
        "year": "",
        "url": ""
    }

# Example usage
# results = search("bella")
# print(results)
