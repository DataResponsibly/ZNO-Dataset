"""Shorten the text to remove human factor."""
import re
from src.constants import NAME_UPDATER_1, NAME_UPDATER_2


def shorten(text: str) -> str:
    """Shorten the text to remove human factor.

    Args:
        text: Text to shorten.

    Returns:
        str: Shortened text.
    """
    
    for ab in NAME_UPDATER_1:
        text = text.replace(ab, NAME_UPDATER_1[ab])

    text = re.sub(r'[\s\r\n\t]+', '', text)
    text = (
        text.replace('IIII', '3')
        .replace('III', '2')
        .replace('ІІІІ', '3')
        .replace('ІІІІ', '3')
        .replace('ІІІ', '2')
        .lower())
    
    text = text if (len(text) and text[-1].isdigit()) else text[:-1]

    return text


def ukr_schools_shorten(text: str) -> str:
    """Shorten the text to remove human factor.

    This function contains some specific text replacements for Ukrainian
    schools datasets.

    Args:
        text: Text to shorten.

    Returns:
        str: Shortened text.
    """
    text = shorten(text)
    
    for symb in NAME_UPDATER_2:
        text = text.replace(symb, NAME_UPDATER_2[symb])

    text = text.replace('"', '').replace(r'\\', '')
    return text
