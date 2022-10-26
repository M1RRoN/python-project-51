import argparse
import os


def pars():
    parser = argparse.ArgumentParser(description='Page Loader')
    parser.add_argument('url_page', type=str)
    parser.add_argument('-o', '--output',
                        type=str,
                        default=os.getcwd(),
                        help='downland_path')
    args = parser.parse_args()
    return args.url_page, args.output
