def site_name(url: str) -> str:
    url = url.replace('https://', '').replace('.', '-').replace('/', '-')
    url = ''.join(url)
    return url + '.html'
