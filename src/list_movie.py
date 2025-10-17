def list_movie(movie_list: list, my_genre: str) -> list:
    """Функция выводит фильмы по жанрам"""
    return [i for i in movie_list if i["genre"] == my_genre]
    # new_movie = []
    # for i in movie_list:
    #      if i['genre'] == my_genre:
    #         new_movie.append(i)
    #
    # return new_movie
