# -*- coding: utf-8 -*-
# --- author: wtavares
# --- Web Aplication Functions

import logging
import requests
import settings as cfg


def github_do_update():

    data = github_get_update_data()

    return True


def github_get_update_data():

    logging.debug("Getting from GitHUB API")

    url = _git_get_api()

    ret = requests.get(url)

    data = None

    if ret.status_code == 200:
        logging.debug('GitHUB request OK')
        js = ret.json()
        if 'items' in js:
            data = js['items']

    else:
        logging.debug('GitHUB request FAILED')

    return data


def _git_get_api():

    ret = cfg.GIT_API+'?'

    query = 'q='
    for l in cfg.GIT_LANGS:
        query += 'language:{}+'.format(l)

    order = "sort={}".format(cfg.GIT_SORT)

    ret += query+'&'+order

    return ret
