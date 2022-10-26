import pytest
from page_loader.loader import site_name


def test_site_name():
    assert site_name('https://ru.hexlet.io/courses') == 'ru-hexlet-io-courses.html'