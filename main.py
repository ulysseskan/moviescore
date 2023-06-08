#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created: Thu Dec 30 14:38:11 2021
Updated: Thu Jun 8 14:31:00 2023

Original author: julienpezet https://github.com/JulienPezet/get_movie_score
Modified by: Ulysses
"""

import sys
from get_score import find_rt, find_imdb

# Check if the movie query name is provided as a command-line argument
if len(sys.argv) < 2:
    print("Usage: python3 main.py <movie_query>")
    sys.exit(1)

# Extract the movie query from command-line arguments
QUERY = " ".join(sys.argv[1:])

tomatometer = find_rt(QUERY)
imdbscore = find_imdb(QUERY)
print(f"IMDB Score: {imdbscore}")
if not tomatometer:
    print("This movie has no Rotten Tomatometer score yet.")
else:
    print(f"Tomatometer: {tomatometer}\n")
