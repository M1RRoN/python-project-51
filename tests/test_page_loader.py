import pytest
from page_loader.page_loader import site_name


def test_site_name():
    assert site_name('https://ru.hexlet.io/courses') == 'ru-hexlet-io-courses.html'