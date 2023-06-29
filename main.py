#!/usr/bin/env python3
"""
Gets IMDb, RottenTomatoes, Cinemascore, Letterboxd, and CommonSenseMedia ratings for a given movie.

Original author: julienpezet https://github.com/JulienPezet/get_movie_score
Modified by: Ulysses
"""
import sys
# import cProfile
import cinemascore
import letterboxd
import myimdb as im
import mytomatoes as rt
import csm

# Check if the movie query name is provided as a command-line argument
if len(sys.argv) < 2:
    print("Usage: python3 main.py <movie_query>")
    sys.exit(1)

# Extract the movie query from command-line arguments
QUERY = " ".join(sys.argv[1:])


def print_movie_info(movie_info, matching_years):
    """Print movie info if years match"""
    if movie_info and movie_info['year'] in matching_years:
        if 'url' in movie_info:
            print(f"{movie_info['url']}")
        if movie_info['title'] is not None:
            print(f"{movie_info['title']}, {movie_info['year']}")
        if 'rating' in movie_info:
            print(f"Rating: {movie_info['rating']}")
        if 'one_liner' in movie_info:
            print(f"{movie_info['one_liner']}")
        print()


def main():
    """Gather movie data"""
    # Variables to store title and scores
    rt_result = rt.search(QUERY)
    im_results = im.search(QUERY)
    cs_result = cinemascore.search(QUERY)
    lb_result = letterboxd.search(QUERY)
    csm_result = csm.search(QUERY)

    # Gather the years from rt, lb, and cs results
    years = [result['year'] for result in [rt_result, lb_result, cs_result, csm_result] if result]

    # Find most common year in list of years
    if years and len(set(years)) >= 1:
        matching_year = max(set(years), key=years.count)  # Get the most common year
        # Create a new list with only the years that match the most common year
        matching_years = [year for year in years if year == matching_year]

        # Print the results only if the years match
        if im_results:
            for result in im_results:
                if result['year'] in matching_years:
                    print(f"{result['url']}parentalguide")
                    print(f"{result['title']}, {result['year']}")
                    print(f"Rating: {result['rating']}")
                    print()

        print_movie_info(rt_result, matching_years)
        print_movie_info(lb_result, matching_years)
        print_movie_info(cs_result, matching_years)
        print_movie_info(csm_result, matching_years)

    else:
        print(f"DEBUG Years - RT: {rt_result['year'] if rt_result else 'N/A'},"
            f" LB: {lb_result['year'] if lb_result else 'N/A'},"
            f" CS: {cs_result['year'] if cs_result else 'N/A'},"
            f" CSM: {csm_result['year'] if csm_result and 'year' in csm_result else 'N/A'}")

# Wrap with the profiler
# cProfile.run('main()', sort='tottime')

main()
