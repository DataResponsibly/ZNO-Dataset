"""A scripts specific for Ukrainian schools."""
from src.check_site import search_text, logging
from src.shorteners import ukr_schools_shorten as shorten
import csv
import time
from tqdm import tqdm

def search(text: str, url: str) -> int:
    """Run the script.

    Args:
        text: Text to search.
        url: Url to search.

    Returns:
        int: ЄДРПОУ of the school if text is present on the page,
        0 otherwise.
    """
    if not url:
        return "Not found."
    page_text = "429toomanyrequests"
    while "429toomanyrequests" in page_text:
        found, page_text = search_text(text, url, shorten)
        if found:
            logging.info(f"'{text}' is present on the page '{url}'.")
            return int(url.split("/")[-1].split("?")[0])
        if "429toomanyrequests429toomanyrequestsopenresty" in page_text:
            logging.error("Too many requests. Waiting 10 seconds.")
            time.sleep(10)
            continue
        logging.warning(f"'{text}' is not present on the page '{url}'.")
        logging.debug(f"Shortened text: '{shorten(text)}'.")
        logging.debug(f"Text from the page: \n\nSTART\n{page_text}\nEND\n\n")
        return "Not found."
    return "Not found."


def write_nums_to_csv(nums: list[tuple[str, str, int]]) -> None:
    """Write nums to csv file.

    Args:
        nums: List of tuples (text, url, num).
    """
    with open("data/checked_links.csv", "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(nums)


def parse_schools(file: str) -> None:
    """Open csv file and search each text on the corresponding url.

    Args:
        file: Path to csv file.

    Raises:
        KeyboardInterrupt: If the user presses Ctrl+C.
    """
    nums: list[tuple[str, str, int]] = []

    with open(file, "r") as csv_file:
        reader = csv.reader(csv_file)
        next(reader, None)  # skip the headers
        
        try:
            for row in tqdm(reader):
                if not row[-1]:
                    continue
                num = search(row[0], row[-1]) # extract eoname and url
                if num:
                    logging.info(f"ЄДРПОУ: {num}")
                nums.append((row[0], row[-1], num))# extract eoname and url
                time.sleep(2)
                write_nums_to_csv(nums)
        except KeyboardInterrupt:
            logging.error("Keyboard interrupt.")
            write_nums_to_csv(nums)
            raise
    write_nums_to_csv(nums)

if __name__ == "__main__":
    parse_schools("data/unmatched_link.csv")