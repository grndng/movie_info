# if not installed, you can install the package with
# pip install cinemagoer or 
# pip3 install cinemagoer

from imdb import Cinemagoer

def get_movie_data(movie_file: str, output_file: str) -> None:
    """Scrape movie data based on a file passed to the function

    Args:
        movielist (str): path to text file that contains movie list
        output_file (str): path to output file with metadata
    """
    movielist = []
    with open(movie_file, "r") as f:
        for lines in f.readlines():
            _, movie = lines.split("-")
            movie = movie.strip()
            movielist.append(movie)
        movielist = sorted(movielist)

    ia = Cinemagoer()
    with open(output_file, "a") as file:
        for movie in movielist:
            print(f"Getting data for '{movie}'.")
            movie_id = ia.search_movie(movie)[0].movieID
            movie = ia.get_movie(movie_id)
            file.write(f"- {movie} ({movie.get('year')}); {movie.get('rating')}/10; (on [IMDb](https://www.imdb.com/title/tt{movie_id}))\n")

        f.close()

get_movie_data("movie_recommendations.txt", "output.txt")