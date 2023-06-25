"""Get movie rating from Letterboxd"""
from letterboxdpy import movie

def search(query):
    """Search for a movie title"""
    movie_title = query

    try:
        # Create a Movie object with the lowercase movie title
        movie_obj = movie.Movie(movie_title.lower())

        # Capitalize the first letter of each word in the movie title
        capitalized_title = movie_obj.title.title()

        return {'title': capitalized_title, 'rating': movie_obj.rating, 'year': movie_obj.year, \
                'url': movie_obj.url}

    except AttributeError:
        return None
    except Exception as error:
        if str(error) == "No movie found":
            return None
        raise error  # Re-raise the exception for other errors
