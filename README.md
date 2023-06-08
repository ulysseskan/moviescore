## tl;dr
Gets movie ratings from IMDb and RottenTomatoes for a given movie

## About
Fork of https://github.com/JulienPezet/get_movie_score
- Uses latest available (sometimes unofficial) APIs as of June 2023
- Conforms a bit better to python standards

< screenshot will be added once more of the improvements below are put in >

## Getting Started

1. ```git clone https://github.com/ulysseskan/moviescore.git```
2. ```cd moviescore```
3. ```pip3 install -r requirements.txt```
4. ```python3 main.py <movie query>```

### Prerequisites

You need a copy of Python 3.  I only tested with Python 3.10.  One way to install Python 3 is:

1. Install [Brew](https://brew.sh).
2. ```brew install python3```
3. Ensure Brew's executable bin directory is in your PATH variable, for example:<br>
```echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.profile```

## Potential improvements

- [ ] Add RT audience score
- [ ] Add Cinemascore
- [ ] Add Letterboxd rating
- [ ] Add various parents guide site scores (CommonSenseMedia age rating, Spotlight, MovieGuide, IMDb parental guide excerpt, etc. )
- [ ] Add movie length
- [ ] Colorize output (if score less than x, make red, etc.)
- [ ] Prune requirements.txt

## Bugs and Limitations

- Does not currently show name of the movie Rotten Tomatoes is getting the score for.  This will be fixed shortly.

## License

Distributed under the MIT License. See `LICENSE` for more information.
