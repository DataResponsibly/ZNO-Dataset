# ZNO-Dataset

## Overview

ZNO-Dataset is a repository containing scripts, notebooks, and documentation for processing and analyzing Ukrainian standardized testing data. The project covers data loading, cleaning, transformation into normalized tables, database setup using Docker, and analysis of EIE(ZNO) exams.

## Folder Structure

- **data_loader/**  
  Contains raw data directories (2016–2024) and the main script for loading data: [`load_zno.py`](data_loader/load_zno.py).

- **db_info/**  
  Contains database-related files including the PostgreSQL schema: [`db_schema.sql`](db_info/db_schema.sql) and a Jupyter notebook to test the connection: [`test_connection.ipynb`](db_info/test_connection.ipynb). See also the database setup guide in [`db_info/README.md`](db_info/README.md).

- **notebooks/**  
  Includes Jupyter notebooks for data analysis and table creation. For example, visit the [tables creation README](notebooks/tables_creation/README.md) for more details.

- **datasheet.md**  
  A comprehensive datasheet outlining the dataset's motivation, composition, collection process, and maintenance. Refer to [`datasheet.md`](datasheet.md) for details.

- **Dockerfile**  
  Used to build a Docker image for setting up the PostgreSQL database.

- Additional directories include logs, images, and supporting files.

## Setup Instructions

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/<username>/ZNO-Dataset.git
   cd ZNO-Dataset
   ```

2. **Setup the Database using Docker:**

   Follow the instructions in [`db_info/README.md`](db_info/README.md) or run:

   ```sh
   docker build -t my_db .
   docker run -p 5432:5432 my_db
   psql --host=127.0.0.1 --port=5432 --username=myuser --dbname=EIE
   ```

3. **Load and Process Data:**

   Run the data loader script:

   ```sh
   python data_loader/load_zno.py
   ```

4. **Explore the Notebooks:**

   Open the Jupyter notebooks in the `notebooks` directory for data analysis and table creation.

## Data Documentation

For detailed information on the dataset’s composition, collection, preprocessing, and usage, refer to [`datasheet.md`](datasheet.md).

## Contact

If you need any help, please contact us at [t.herasymova@ucu.edu.ua](t.herasymova@ucu.edu.ua) or open an issue on GitHub.

## License

This project is licensed under the MIT License.