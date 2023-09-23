#!/usr/bin/python3
"""Get a text and a url.

Search whether the text is present on the page.
"""

import datetime
import logging
import os
from typing import Callable

import requests
from bs4 import BeautifulSoup

now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d-%H-%M")
filename = f"logs/{date}.log"
if not os.path.exists("logs"):
    os.makedirs("logs")
logging.basicConfig(
    filename=filename,
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
console = logging.StreamHandler()
console.setLevel(logging.WARNING)
formatter = logging.Formatter("%(levelname)s %(message)s")
console.setFormatter(formatter)
logging.getLogger("").addHandler(console)


HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:116.0) "
    "Gecko/20100101 Firefox/116.0.3"
}


def search_text(
    text: str, url: str, shorten: Callable = lambda x: x
) -> tuple[bool, str]:
    """Check whether the text is present on the page.

    Because of human factor, check the presence of text by removing
    the spaces and converting the text to lowercase.

    Because of different site settings, do parsing
    with javascript disabled and user-agent changed.

    Args:
        text: Text to search.
        url: Url to search.
        shorten: Function to shorten the text.

    Returns:
        tuple[bool, str]: True if text is present on the page,
        False otherwise. Also returns the text from the page.
    """
    text = shorten(text)
    try:
        response = requests.get(url, headers=HEADERS)
    except requests.exceptions.ConnectionError:
        logging.error(f"Connection error on the page '{url}'.")
        return False, ""
    soup = BeautifulSoup(response.text, "html.parser")
    for script in soup(["script", "style"]):
        script.extract()
    text_from_page = soup.get_text()
    text_from_page = shorten(text_from_page)
    return text in text_from_page, text_from_page
