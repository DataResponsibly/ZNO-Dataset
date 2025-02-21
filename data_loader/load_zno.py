'''module to load datasets from open data portal'''

import os
import py7zr
import logging
import requests
import pandas as pd

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__).setLevel(logging.INFO)

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

def download_and_extract(url: str, datadir: str, remote_fname: str, file_name: str, delete_download: bool=False) -> None:
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
    response = requests.get(url)
    with open(download_path, 'wb') as handle:
        handle.write(response.content)

    # Extract the file
    with py7zr.SevenZipFile(download_path, 'r') as archive:
        filename = [i.filename for i in archive.list() if i.filename.endswith('.csv')][0]
        archive.extract(targets=filename, path=datadir)

    # if file in some other directory, move it to datadir and delete this one
    if os.path.join(datadir, filename) != os.path.join(datadir, file_name):
        os.rename(os.path.join(datadir, filename), os.path.join(datadir, file_name))
        # get filename dir and delete it
        os.rmdir(os.path.join(datadir, filename.split('/')[0]))

    # Delete the downloaded file if required and it is not the same as the file in datadir
    if delete_download and download_path != os.path.join(datadir, file_name):
        os.remove(download_path)


def initialize_and_download(datadir: str, year: int, download: bool=False) -> str:
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
        raise FileNotFoundError(f'Could not find {year} ZNO data for in {datadir}. Call get_data with download=True to download the dataset.')

    logging.info(f'Downloading data for {year} data...')
    exam_name = test_type(year)
    
    # Download and extract file
    base_url= 'https://zno.testportal.com.ua/yearstat/uploads'
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
        logger.error(f'\n{os.path.join(datadir, remote_fname)} may be corrupted. Try deleting it and rerunning this command.')
        logger.error('Exception: ', e)
    return file_path

def load_zno(root_dir: str, year: int=2016, download=False) -> pd.DataFrame:
    """
    Load sample of ZNO data from Testportal into DataFrame.
    """
    if year < 2016:
        raise ValueError('Year must be >= 2016')
    elif year > 2023:
        raise ValueError('Year must be <= 2023')

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
        return pd.read_csv(file_name, sep=";", encoding='utf-8')
    except:
        return pd.read_csv(file_name, sep=";", encoding='Windows 1251')

if __name__ == "__main__":
    for year in range(2016, 2024):
        print(load_zno('data_loader', year=year, download=True))
