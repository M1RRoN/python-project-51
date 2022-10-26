import pytest
from page_loader.rename import get_rename


def test_rename():
    assert get_rename('https://ru.hexlet.io/courses') == 'ru-hexlet-io-courses.html'