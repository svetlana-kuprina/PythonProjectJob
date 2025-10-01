from src.list_movie import list_movie


def test_list_movie():
    assert list_movie ([
    {"title": "The Shawshank Redemption", "genre": "Drama", "director": "Frank Darabont"},
    {"title": "The Godfather", "genre": "Crime", "director": "Francis Ford Coppola"},
    {"title": "The Dark Knight", "genre": "Action", "director": "Christopher Nolan"},
], "Drama") == [{'title': 'The Shawshank Redemption', 'genre': 'Drama', 'director': 'Frank Darabont'}]