import requests
from rename import get_path


def download_site(url, dir_path):
    req = requests.get(url)
    html = req.text
    html_path = get_path(dir_path, url)
    with open(html_path, 'w', encoding='utf-8') as file:
        file.write(html)
    return html_path
