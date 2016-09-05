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
