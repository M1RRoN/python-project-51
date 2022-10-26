from urllib.parse import urlparse
import os


def cut_url(url: str) -> str:
    url_parser = urlparse(url)
    clear_url = url_parser.netloc + url_parser.path
    return clear_url


def get_rename(url: str) -> str:
    clear_url = cut_url(url)
    clear_url = clear_url.replace('.', '-').replace('/', '-')
    clear_url = ''.join(clear_url)
    return clear_url + '.html'


def get_path(path, url):
    rename_file = get_rename(url)
    new_path = os.path.join(path, rename_file)
    return new_path
