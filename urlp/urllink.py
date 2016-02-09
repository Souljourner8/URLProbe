"""
All URL related methods
"""

"""
Import libraries
"""

import httplib2                         # Comprehensive HTTP client library
import itertools                        # Comprehensive iterrstion library
import re                               # Regular expression library
from urllib import urlencode            # Method to properly encode a URL string
from collections import defaultdict     # Replacement for default dict()

"""
Import modules
"""

from conversions import *               # Conversion methods


def load_url(url):
    """
    Open and send GET request
    :param url: URL str
    :return: content
    """

    socket = httplib2.Http(".cache")
    socket.follow_all_redirects = True
    resp, content = socket.request(str(url), "GET")
    # assert resp.status == 200
    # assert resp['content-type'] == 'txt/html'
    return [resp, content]


def lcount(content):
    """
    Count the number of links
    :param content: contents of url
    :return: tuple (# of links, list of links found without duplicates
    """

    links = re.findall('"((http|ftp)://.*?)"', to_unicode(content))

    return len(links), links


"""
Variables to keep track of things for mlcount
"""
link_info = [0, []]


def mlcount(content):
    """
    Count total links stemming from url
    :param content: contents of url
    :return: (# of links, list of links found without duplicates
    """

    if lcount(content)[0] == 0:
        return link_info
    else:
        links = lcount(content)[1]
        link_info[1].append(links)
        link_info[0] += lcount(content)[0]
        for link in links[0]:
            if len(link) > 7:
                branch = load_url(link)
                mlcount(branch[1])

        return link_info
