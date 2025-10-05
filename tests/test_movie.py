import pytest


@pytest.mark.parametrize("movie_list1, my_genre1, expected1", [
                                                                    [{"title": "The Shawshank Redemption",
                                                                     "genre": "Drama", "director": "Frank Darabont"},
                                                                    {"title": "The Godfather", "genre": "Crime",
                                                                     "director": "Francis Ford Coppola"},
                                                                    {"title": "The Dark Knight", "genre": "Action",
                                                                     "director": "Christopher Nolan"}],
                                                                    "Drama",
                                                                [{'title': 'The Shawshank Redemption', 'genre': 'Drama',
                                                                  'director': 'Frank Darabont'}]
])
def test_movie(movie_list1, my_genre1, expected1):
    assert (movie_list1, my_genre1) == expected1
