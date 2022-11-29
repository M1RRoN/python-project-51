# !/usr/bin/env python3
# import os
import sys
from page_loader import download
from page_loader.cli import parse
import logging


def main():
    logging.basicConfig(level=logging.INFO)
    try:
        args = parse()
        html_path = download(
            args.url,
            args.output
        )
        print(html_path)
    except Exception as ex:
        logging.error(ex)
        logging.info('Page not found or status_code is not 200')
        sys.exit(1)


if __name__ == '__main__':
    main()
