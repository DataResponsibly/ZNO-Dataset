# Setting Up the EIE Database with Docker

This guide will help you set up a PostgreSQL database for the EIE dataset using Docker. Follow the instructions below to build and run the Docker container, and connect to the database using `psql`.

## Prerequisites

- Docker installed on your machine
- Access to the EIE dataset files

## Folder Structure

Ensure you have the following folder structure in your project:

```
root/
│
├── db_info/
│   ├── db_schema.sql
│   └── test_connection.ipynb
├── notebooks/
│   ├── tables_creation/
│   │   └── final_tables/
│   │       ├── locations_base.csv
│   │       ├── years.csv
│   │       ├── schools_edrpou.csv
│   │       ├── school_stats.csv
│   │       ├── students.csv
│   │       ├── subjects.csv
│   │       ├── test_centers_edrpou.csv
│   │       └── students_take_tests.csv
└── Dockerfile
```

## Setup Instructions

1. Open a terminal and navigate to the root directory of your project.
2. Build the Docker image:

    ```sh
    docker build -t my_db .
    ```

3. Run the Docker container:

    ```sh
    docker run -p 5432:5432 my_db
    ```

4. Connect to the PostgreSQL database using `psql`:

    ```sh
    psql --host=127.0.0.1 --port=5432 --username=myuser --dbname=EIE
    ```

5. List the tables to verify the database setup:

    ```sh
    \dt
    ```

## Connecting with Python

In the `db_info/test_connection.ipynb` file, you can find a small Python script that demonstrates how to connect to the database and provides some SQL examples to query the database.

## ER Diagram

You can find the ER diagram for the EIE database by following this [link](https://docs.google.com/presentation/d/12pYsEAfbL02B18XaxiVKKt37p3-mMSexe7Mzbd5LTr4/edit?usp=sharing).