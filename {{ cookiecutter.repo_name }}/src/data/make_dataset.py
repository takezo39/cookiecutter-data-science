# -*- coding: utf-8 -*-
from dotenv import find_dotenv, load_dotenv
from {{cookiecutter.repo_name}}.data import logger

def main():
    logger.info('making final data set from raw data')


if __name__ == '__main__':

    from {{cookiecutter.repo_name}} import create_argument_parser
    import argparse

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        parents=[create_argument_parser()])

    args = parser.parse_args()

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()

