import os


#a = os.path.splitexet(url)


def site_name(url: str) -> str:
    b = url.replace('https://', '').replace('.', '-').replace('/', '-')
    b = ''.join(b)
    return b + '.html'
print(site_name('https://ru.hexlet.io/courses'))