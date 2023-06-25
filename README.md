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

- [x] Add RT audience score
- [x] Add Cinemascore
- [x] Add Letterboxd rating
- [ ] Add various parents guide site scores (CommonSenseMedia age rating (done), Spotlight, MovieGuide, IMDb parental guide excerpt, etc. )
- [x] Add movie length
- [ ] Make it hostable on a (local) web server
- [ ] Colorize output (if score less than x, make red, etc.)
- [ ] Add prediction "you'll probably like it" if CinemaScore >= B, RottenTomatoes better than 55%+, MovieGuide better than -2, IMDb 6+, Letterboxd 3+ and vice versa
- [ ] Prune requirements.txt

## Bugs and Limitations

- Searching for interstellar does not return expected results
- Searching for king kong 1933 does not return expected results

## License

Distributed under the MIT License. See `LICENSE` for more information.
