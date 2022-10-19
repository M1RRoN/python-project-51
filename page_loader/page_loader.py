def site_name(url: str) -> str:
    b = url.replace('https://', '').replace('.', '-').replace('/', '-')
    b = ''.join(b)
    return b + '.html'
