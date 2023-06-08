#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Original author: julienpezet https://github.com/JulienPezet/get_movie_score
Modified by: Ulysses
"""

import rottentomatoes as rt
import imdb
ia = imdb.Cinemagoer()

def find_rt(query):
    """Get Tomatometer Score"""
    result = rt.tomatometer(query)  # Query the search results

    if result is not None:
        return result

    print("This movie has no Rotten Tomatometer score yet.")
    return []

def find_imdb(query):
    """Get iMDB score"""
    movies = ia.search_movie(query)      # Query search results
    imdb_id = movies[0].getID()          # Take the first one (IMDb API is quite good so far)
    movie = ia.get_movie(imdb_id)        # Get data with ID
    title = movie['title']
    year = movie['year']
    rating = int(movie['rating']*10)
    directors = movie['directors'][0]['name']
    casting = movie['cast'][0]['name']
    print(f"IMDb found: {title} ({year}), by {directors} with {casting}\n")
    return rating
