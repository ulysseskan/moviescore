"""IMDb movie url + rating fetcher"""
from urllib.parse import urlsplit, urlunsplit
import requests
from bs4 import BeautifulSoup

def search(query):
    """Get IMDb scores, release year, titles, and URLs for a given movie query"""
    url = f"https://m.imdb.com/find/?q={query}&s=tt&ttype=ft&exact=true"
    headers = {'User-Agent': 'Mozilla/5.0 \
               (iPhone; CPU iPhone OS 14_0 like Mac OS X) \
               AppleWebKit/605.1.15 (KHTML, like Gecko) \
               Version/14.0 Mobile/15E148 Safari/604.1'}
    response = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    first_result = soup.select_one(".ipc-metadata-list-summary-item__tc")
    if first_result is None:
        return []

    imdb_title = first_result.select_one(".ipc-metadata-list-summary-item__t").text.strip()
    imdb_url = "https://m.imdb.com" + first_result.select_one("a")["href"]

    # Clicked movie detail page
    movie_response = requests.get(imdb_url, headers=headers, timeout=10)
    movie_soup = BeautifulSoup(movie_response.text, "html.parser")

    # Extract release year from the title tag
    title_tag = movie_soup.select_one("title")
    release_year = title_tag.text.strip().split("(")[-1].split(")")[0]

    imdb_rating = movie_soup.select_one("span.sc-bde20123-1.iZlgcd")
    imdb_rating = imdb_rating.text.strip() if imdb_rating else None

    if imdb_rating is None:
        print("IMDb rating not found. Soup object (excerpt):")
        print(movie_soup.select_one(".ipc-metadata-list-summary-item__tc"))

    # Strip the ref part from the IMDb URL
    imdb_url_parts = urlsplit(imdb_url)
    imdb_url_parts = imdb_url_parts._replace(query='', fragment='')
    imdb_url_stripped = urlunsplit(imdb_url_parts)

    return [{'title': imdb_title, 'rating': imdb_rating, 'year': release_year, \
             'url': imdb_url_stripped}]

# result = search("king kong")
# print(result)
