'''module to load datasets from open data portal'''

import os
import py7zr
import logging
import requests
import pandas as pd

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def test_type(year: int) -> str:
    """Return the type of test based on the year."""
    if year >= 2022:
        return 'NMT'
    return 'ZNO'

def download_and_extract(url, datadir, remote_fname, file_name, delete_download=False): # TODO: typehinting
    """Helper function to download and unzip files."""
    download_path = os.path.join(datadir, remote_fname)
    response = requests.get(url)
    with open(download_path, 'wb') as handle:
        handle.write(response.content)

    with py7zr.SevenZipFile(download_path, 'r') as archive:
        filename = [i.filename for i in archive.list() if i.filename.endswith('.csv')][0]
        archive.extract(targets=filename, path=datadir)

    # if file in some other directory, move it to datadir and delete this one
    if os.path.join(datadir, filename) != os.path.join(datadir, file_name):
        os.rename(os.path.join(datadir, filename), os.path.join(datadir, file_name))
        # get filename dir and delete it
        os.rmdir(os.path.join(datadir, filename.split('/')[0]))

    if delete_download and download_path != os.path.join(datadir, file_name):
        os.remove(download_path)


def initialize_and_download(datadir: str, year: int, download: bool=False) -> str:
    """Download the dataset (if required)."""
    assert int(year) >= 2016

    if int(year) >= 2019:
        file_name = f'Odata{year}File.csv'
    else:
        file_name = f'OpenData{year}.csv'

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
        download_and_extract(url, datadir, remote_fname, file_name, delete_download=True)
    except Exception as e:
        logging.error(f'\n{os.path.join(datadir, remote_fname)} may be corrupted. Try deleting it and rerunning this command.')
        logging.error('Exception: ', e)
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
