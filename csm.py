"""
Searches CommonSenseMedia for a given movie and returns url, title, age rating, year, one-liner
"""
import re
import requests
from bs4 import BeautifulSoup

def search(query):
    """Search CSM for movies and return url, title, age rating, year, and one-line review"""
    url = f"https://www.commonsensemedia.org/search/category/movie/{query}"
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.content, "html.parser")

    result = {}

    # Find review title and return URL
    review_title = soup.find("h3", class_="review-title")
    if review_title:
        review_url = "https://www.commonsensemedia.org" + review_title.a["href"]
        result["title"] = review_title.text.strip()
        result["url"] = review_url

    # Find rating age and return it
    rating_age = soup.find("span", class_="rating__age")
    if rating_age:
        result["rating"] = rating_age.text.strip()

    # Find product summary and extract year
    product_summary = soup.find("div", class_="review-product-summary")
    if product_summary:
        year_span = product_summary.find("span", string=re.compile(r"Release Year:\s+(\d{4})"))
        if year_span:
            year_match = re.search(r"(\d{4})", year_span.text)
            if year_match:
                result["year"] = year_match.group(1)

    # Find one-liner and return it
    one_liner = soup.find("p", class_="review-one-liner")
    if one_liner:
        result["one_liner"] = one_liner.text.strip()

    return result
