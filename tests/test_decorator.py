import pytest

from src.Decorator import shorten_words


def test_shorten_words():
    @shorten_words(8)
    def words(text):
        return text

    assert words(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit.") == "Lorem ipsum dolor sit amet, consecte. adipisci. elit."

def test_shorten_words2():
    @shorten_words(10,end_symbol='?')
    def words(text):
        return text

    assert words(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit.") == "Lorem ipsum dolor sit amet, consectetu? adipiscing elit."
