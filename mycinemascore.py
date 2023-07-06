"""Get Cinemascore Grade for a Given Movie Title"""
# cinemascore.py
# Licensed under the MIT License
# Original: https://github.com/jhumms/Cinemascore-api
# Modified by: Ulysses

import json
from base64 import b64encode
import requests

def search(query):
    """Search Cinemascore for a movie title"""
    encoded_query = b64encode(query.encode('utf-8')).decode('utf-8')
    response = requests.get("https://webapp.cinemascore.com/guest/search/title/" + encoded_query, \
                            timeout=10).text
    data = json.loads(response)
    display_url = "https://www.cinemascore.com/"

    if data:
        try:
            first_movie = data[0]
            title = first_movie['TITLE']
            rating = first_movie['GRADE']
            year = first_movie['YEAR']
            return {'title': title, 'rating': rating, 'year': year, 'url': display_url}
        except KeyError:  # if result is undefined/not available, catch and return None
            pass

    return None
