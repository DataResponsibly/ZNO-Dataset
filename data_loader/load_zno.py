'''module to load datasets from open data portal'''

import os
import py7zr
import logging
import requests
import pandas as pd

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def test_type(year: int) -> str:
    """
    Return the type of test based on the year.

    Args:
        year (int): The year of the test.

    Returns:
        str: The type of test.
    """
    if year >= 2022:
        return 'NMT'
    return 'ZNO'


def file_structure(year: int) -> str:
    """
    Return the file structure based on the year.

    Args:
        year (int): The year of the test.

    Returns:
        str: The file structure.
    """
    if year >= 2019:
        return f'Odata{year}File.csv'
    return f'OpenData{year}.csv'


def download_and_extract(
    url: str,
    datadir: str,
    remote_fname: str,
    file_name: str,
    delete_download: bool = False
) -> None:
    """
    Helper function to download and unzip files.

    Args:
        url (str):              The URL to download the file from.
        datadir (str):          The directory to save the file to.
        remote_fname (str):     The name of the file to download.
        file_name (str):        The name of the file to extract.
        delete_download (bool): Whether to delete the downloaded file.

    Returns:
        None
    """
    # Download the file
    download_path = os.path.join(datadir, remote_fname)
    response = requests.get(url, timeout=60)
    response.raise_for_status()
    with open(download_path, 'wb') as handle:
        handle.write(response.content)

    # Extract all files to a temporary directory
    temp_extract_dir = os.path.join(datadir, '_temp_extract')
    os.makedirs(temp_extract_dir, exist_ok=True)
    
    with py7zr.SevenZipFile(download_path, 'r') as archive:
        archive.extractall(path=temp_extract_dir)

    # Locate the CSV file that was extracted
    extracted_csv_path = None
    for root, _dirs, files in os.walk(temp_extract_dir):
        for fname in files:
            if fname.lower().endswith('.csv'):
                candidate = os.path.join(root, fname)
                # Prefer the expected name if present
                if fname == file_name:
                    extracted_csv_path = candidate
                    break
                # Otherwise remember the first CSV found
                if extracted_csv_path is None:
                    extracted_csv_path = candidate
        if extracted_csv_path is not None:
            break

    if extracted_csv_path is None:
        raise FileNotFoundError(
            f'No CSV found after extracting {remote_fname} into {temp_extract_dir}'
        )

    # Move the CSV to the expected location in datadir (not in subdirectory)
    final_path = os.path.join(datadir, file_name)
    os.replace(extracted_csv_path, final_path)

    # Clean up temporary extraction directory
    import shutil
    try:
        shutil.rmtree(temp_extract_dir)
    except Exception as e:
        logger.warning(f'Could not remove temporary directory {temp_extract_dir}: {e}')

    # Delete the downloaded archive if required
    if delete_download:
        try:
            os.remove(download_path)
        except Exception as e:
            logger.warning(f'Could not remove downloaded file {download_path}: {e}')


def initialize_and_download(datadir: str, year: int, download: bool = False) -> str:
    """
    Download the dataset (if required).
    
    Args:
        datadir (str):   The directory to save the file to.
        year (int):      The year of the test.
        download (bool): Whether to download the file.

    Returns:
        str: The path to the downloaded file.
    """
    assert int(year) >= 2016
    file_name = file_structure(year)

    # Assume is the path exists and is a file, then it has been downloaded
    file_path = os.path.join(datadir, file_name)
    if os.path.isfile(file_path):
        return file_path
    if not download:
        raise FileNotFoundError(
            (
                f'Could not find {year} ZNO data in {datadir}. '
                'Call get_data with download=True to download the dataset.'
            )
        )

    logging.info(f'Downloading data for {year} data...')
    exam_name = test_type(year)
    
    # Download and extract file
    base_url = 'https://zno.testportal.com.ua/yearstat/uploads'
    remote_fname = f'OpenData{exam_name}{year}.7z'
    url = f'{base_url}/{remote_fname}'
    try:
        download_and_extract(
            url=url, 
            datadir=datadir, 
            remote_fname=remote_fname, 
            file_name=file_name, 
            delete_download=True
        )
    except Exception as e:
        logger.error(
            (
                f"{os.path.join(datadir, remote_fname)} may be corrupted. "
                'Try deleting it and rerunning this command.'
            )
        )
        logger.exception('Download or extraction failed')
    return file_path

def load_zno(
    root_dir: str,
    year: int = 2016,
    download: bool = False
) -> pd.DataFrame:
    """
    Load sample of ZNO data from Testportal into DataFrame.
    """
    # Create directory if it does not exist
    base_datadir = os.path.join(root_dir, str(year))
    os.makedirs(base_datadir, exist_ok=True)

    # Initialize and download the dataset
    file_name = initialize_and_download(
        datadir=base_datadir, 
        year=year, 
        download=download
    )

    try:
        return pd.read_csv(file_name, sep=';', encoding='utf-8')
    except UnicodeDecodeError:
        return pd.read_csv(file_name, sep=';', encoding='Windows 1251')

if __name__ == "__main__":
    for year_ in range(2016, 2026):
        print(load_zno('data_loader', year=year_, download=True))
