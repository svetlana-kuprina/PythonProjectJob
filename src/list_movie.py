def list_movie(movie_list, my_genre):
    """Функция выводит фильмы по жанрам"""
    return [i for i in movie_list if i["genre"] == my_genre]
    # new_movie = []
    # for i in movie_list:
    #     if i['genre'] == my_genre:
    #         new_movie.append(i)
    #
    # return new_movie


a = [
    {"title": "The Shawshank Redemption", "genre": "Drama", "director": "Frank Darabont"},
    {"title": "The Godfather", "genre": "Crime", "director": "Francis Ford Coppola"},
    {"title": "The Dark Knight", "genre": "Action", "director": "Christopher Nolan"},
]
b = "Drama"
print(list_movie(a, b))
