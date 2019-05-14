# -*- coding: utf-8 -*-
# --- author: wtavares
# --- Settings

import logging
import os

# --- Global
DRY_RUN = os.getenv('APP_DRY_RUN', False)

API_TOKEN = '54LKJRH5LKJHE4LKHLKDHKJH4667098094844LKJH6LK6HJ5LKJ4H3LKJ3HKLJHW'
APP_KEY = 'HKJH4667098094844LKJH6LK6HJ5LKJ4'
APP_PORT_DEFAULT = 5000
APP_PORT = os.getenv('PORT', APP_PORT_DEFAULT)


GIT_API = "https://api.github.com/search/repositories"
GIT_LANGS = [
    'java',
    'python',
    'go'
    'php',
    'javascript'
]
GIT_SORT = 'stars'

# --- Logging
LOG_LEVEL = logging.DEBUG
LOG_FILENAME = None

logging.basicConfig(format='[%(asctime)s] [%(levelname)s] %(message)s - [%(filename)s:%(lineno)d]',
                    level=LOG_LEVEL,
                    filename=LOG_FILENAME)
