"""Spotlight movie url + rating fetcher"""
import re
import requests
from bs4 import BeautifulSoup

def search(query):
    """Get Spotlight scores, release year, titles, URLs, and one-liners for a given movie query"""
    response = requests.get(f"https://christiananswers.net/cgi-bin/search/search.cgi?zoom_query={query}&zoom_cat%5B%5D=3", timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    first_result = soup.select_one("div.result_title > a")
    if not first_result:
        print("Spotlight: Movie not found.")
        return {}

    try:
        spot_title = first_result.text.strip().split(" (")[0]  # Extract title portion before " ("
    except AttributeError:
        print("Spotlight: Title element not found.")
        return {}

    spot_url = first_result["href"]  # Remove the hostname from the href value

    # Extract the year from the URL using regular expressions
    year_match = re.search(r"/movies/(\d{4})/", spot_url)
    year = year_match.group(1) if year_match else None

    movie_response = requests.get(spot_url, timeout=10)
    movie_soup = BeautifulSoup(movie_response.text, "html.parser")

    spot_rating = movie_soup.select_one("div.infocoltwo")
    spot_rating = spot_rating.text.strip() if spot_rating else None

    # Only return an empty string if no one liner is found
    one_liner = next((tag.text.strip() for tag in movie_soup.find_all("p") \
                      if tag.text.startswith("Violence: ")), None)

    if spot_rating is None:
        print("Spotlight rating not found.")

    return {'title': spot_title, 'rating': spot_rating, 'year': year, \
             'url': spot_url, 'one_liner': one_liner}

# result = search("king kong")
# print(result)
