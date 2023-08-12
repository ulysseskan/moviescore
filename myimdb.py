"""IMDb movie url + rating fetcher"""
from urllib.parse import urlsplit, urlunsplit
import re
import requests
from bs4 import BeautifulSoup

def search(query):
    """Get IMDb scores, release year, titles, URLs, Parents Guide for a given movie query"""
    url = f"https://m.imdb.com/find/?q={query}&s=tt&ttype=ft&exact=true"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) \
            AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 \
                Safari/605.1.15'
    }
    response1 = requests.get(url, headers=headers, timeout=10)
    soup1 = BeautifulSoup(response1.text, "html.parser")

    first_result = soup1.select_one(".ipc-metadata-list-summary-item__tc")
    if first_result is None:
        return []

    imdb_data = {
        'title': first_result.select_one(".ipc-metadata-list-summary-item__t").text.strip(),
        'url': "https://www.imdb.com" + first_result.select_one("a")["href"],
    }

    # Clicked movie detail page
    response2 = requests.get(imdb_data['url'], headers=headers, timeout=10)
    soup2 = BeautifulSoup(response2.text, "html.parser")

    imdb_data['year'] = soup2.select_one("title").text.strip().split("(")[-1].split(")")[0]

    imdb_data['poster'] = (
        re.search(r'"image":"(https://m.media-amazon.com[^"]+)"', soup2.find("script", type="application/ld+json").text).group(1)
        if soup2.find("script", type="application/ld+json") and re.search(r'"image":"(https://m.media-amazon.com[^"]+)"', soup2.find("script", type="application/ld+json").text)
        else None
    )

    imdb_rating = soup2.select_one("span.sc-bde20123-1.iZlgcd")
    imdb_data['rating'] = imdb_rating.text.strip() if imdb_rating else None

    url_parts = urlsplit(imdb_data['url'])
    parentsguide_url = (
        urlunsplit(url_parts._replace(netloc='www.imdb.com')).rstrip('/?ref_=fn_tt_tt_1')
        + "/parentalguide"
    )

    response3 = requests.get(parentsguide_url, headers=headers, timeout=10)
    soup3 = BeautifulSoup(response3.text, "html.parser")

    imdb_data['url'] = parentsguide_url  # Change the URL to parentsguide_url

    imdb_data['parentsguide'] = {
        section.get("id").replace("advisory-", "").upper(): {
            'status_word': (
                section.select_one("span[class*=ipl-status-pill--]").get("class")[1].split("--")[-1]
                if section.select_one("span[class*=ipl-status-pill--]") else None
            ),
            'li_contents': [
                list_item.get_text(strip=True).replace("Edit", "").strip()
                for list_item in section.select("li.ipl-zebra-list__item")
            ]
        }
        for section in soup3.select("section[id]")
        if "spoiler" not in section.get("id") and section.get("id").startswith("advisory")
    }

    return [imdb_data]

# result = search("arrival")
# print(result)
