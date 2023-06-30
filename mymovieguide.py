"""
Searches MovieGuide for a given movie and returns url, title, rating, year, one-liner
"""
import requests
from bs4 import BeautifulSoup

def search(query):
    """Search MovieGuide for movies and return url, title, age rating, year, and one-line review"""
    url = f"https://www.movieguide.org/?s={query}&cat=195,961,21024,21025"
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.content, "html.parser")

    mg_result = {}

    # Find review title and return URL, year, one_liner
    review_title = soup.find("h2", class_="title")
    if review_title:
        review_url = review_title.a["href"]
        mg_result["title"] = review_title.text.strip()
        mg_result["url"] = review_url

        movie_response = requests.get(review_url, timeout=10)
        movie_soup = BeautifulSoup(movie_response.text, "html.parser")

        release_date_element = movie_soup.find('div', class_='cb-review-box').find('p').find('strong', text="Release Date: ").parent
        if release_date_element:
            release_date_text = release_date_element.text.replace("Release Date: ", "").strip()
            release_date_list = release_date_text.split()
            if release_date_list:
                mg_result["year"] = int(release_date_list[-1])

        i_element = movie_soup.find('h3').find('i')
        if i_element:
            mg_result["one_liner"] = i_element.text

        rating_element = movie_soup.find('span', class_='movieguide_data')
        if rating_element:
            mg_result["rating"] = rating_element.text.strip()

    if "year" not in mg_result:
        mg_result["year"] = '0000'

    if "title" not in mg_result:
        mg_result["title"] = None

    return mg_result

# result = search("king kong")
# print(result)
