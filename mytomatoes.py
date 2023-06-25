"""Get RottenTomatoes score and title for a given movie query"""

import rottentomatoes as rt

def search(query):
    """Get Movie Title, Tomatometer Score, Audience Score"""
    try:
        tomatometer_score = rt.tomatometer(query)
        audience_score = rt.audience_score(query)
        movie = rt.Movie(query)
        rt_inner_url = rt.standalone._movie_url(query)  # pylint: disable=W0212
        output = str(movie)
        rt_inner_title = ' '.join(output.split('\n', maxsplit=2)[:2])
        rt_inner_year = rt.year_released(query)

        return {
            'title': rt_inner_title,
            'url': rt_inner_url,
            'tomatometer': tomatometer_score,
            'audience': audience_score,
            'year': rt_inner_year
        }

    except rt.exceptions.LookupError:
        return {
            'title': None,
            'url': None,
            'tomatometer': None,
            'audience': None,
            'year': None
        }
