# README for `tables_creation` Folder

This directory contains the necessary scripts and data for preprocess raw EIE dataset and normalize it into separate tables, which used for setupping DB and for analysis. Below are the details of the folder.

## Description of Contents

### `fin_data/`
- Contains financial data related to the EIE dataset(Schools).

### `final_tables/`
- Contains CSV files that represent the final versions of various tables used in the EIE database.

### `location_data/`
- Contains data related to locations info and their historical renamings.

### `matching_data/`
- Contains data used for matching various entities within the dataset

### `school_data/`
- Contains data specifically related to schools(manual created matches, which we cannot automize).

### `src/`
- Source files and scripts used in the data processing and table creation.

### Notebooks (`*.ipynb`)
- Various Jupyter notebooks are provided for creating and populating the tables for DB and future data analysis.

## List of Jupyter Notebooks

- `Locations_data.ipynb`: Processes data related to locations.
- `Locations_table.ipynb`: Creates and process the locations table.
- `Organizations_table.ipynb`  **#TODO:** remove this table
- `Schools_stats_table.ipynb`: Creates and process the Schools Finance table.
- `Schools_table.ipynb`:  Creates and process the schools table.
- `Students_Take_Tests.ipynb`: Creates and process the schools take tests with information what scores students have for each test.
- `Students_table.ipynb`: Creates and process the students table, which contains general information about students.
- `Tables_Description.ipynb`: Provides detailed descriptions for created tables.
- `Test_centers_table.ipynb`: Creates and process the test centers table.
- `Tests_table.ipynb`:  Creates and process the tests table.
- `Years_table.ipynb`: Creates and process the years table.
