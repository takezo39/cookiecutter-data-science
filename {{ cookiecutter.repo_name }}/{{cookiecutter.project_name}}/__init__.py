#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
{{cookiecutter.description}}
"""

import os
import logging
import sys

__author__ = "{{cookiecutter.author_name}}"
__copyright__ = "Copyright {{cookiecutter.year}}, {{cookiecutter.company}}"
__version__ = "0.1"
__email__ = "{{cookiecutter.email}}"

base_dir = os.path.dirname(__file__)

# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create STDERR handler
handler = logging.StreamHandler(sys.stderr)

# Create formatter and add it to the handler
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Set STDERR handler as the only handler
logger.handlers = [handler]


def create_argument_parser():
    """Creates general purpose command-line options

    Pass it in as part of the 'parents' argument to your own ArgumentParser.
    More arguments can be added to your own ArgumentParser"""
    import time
    import argparse

    parser = argparse.ArgumentParser(add_help=False)

    parser.add_argument('-month', default=time.strftime("%Y-%m"), type=str,
                        help="Month to be filtered in the form year-month")

    parser.add_argument('-parsedate', default=time.strftime("%Y-%m-%d"),
                        type=str, help="Date for which data will be studied.")

    parser.add_argument('-DB', default="DB", type=str,
                        help='Database to be queried')

    parser.add_argument('-force', action='store_true',
                        help="If True, force processing actions"
                             "and ignore backups.")

    parser.add_argument('-debug', action='store_true',
                        help="Do not run the main function")

    parser.add_argument(
        '--logging_level', default='ERROR',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        help='Set the logging level of detail.')

    return parser
