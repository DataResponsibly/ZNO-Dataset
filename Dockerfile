FROM postgres:latest

# Create a directory to store SQL scripts and CSV files
WORKDIR /usr/src/app

ENV POSTGRES_DB=EIE
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword
#ENV POSTGRES_HOST_AUTH_METHOD=trust

# Copy SQL scripts and CSV files
COPY ./db_info/db_schema.sql .
COPY ./notebooks/tables_creation/final_tables/locations_base.csv final_tables/
COPY ./notebooks/tables_creation/final_tables/years.csv final_tables/
COPY ./notebooks/tables_creation/final_tables/schools_edrpou.csv final_tables/
COPY ./notebooks/tables_creation/final_tables/school_stats.csv final_tables/
COPY ./notebooks/tables_creation/final_tables/students.csv final_tables/
COPY ./notebooks/tables_creation/final_tables/subjects.csv final_tables/
COPY ./notebooks/tables_creation/final_tables/test_centers_edrpou.csv final_tables/
COPY ./notebooks/tables_creation/final_tables/students_take_tests.csv final_tables/

ENV max_wal_size='10GB'

# Run SQL scripts during container initialization
COPY ./db_info/db_schema.sql /docker-entrypoint-initdb.d/

# Expose PostgreSQL default port
EXPOSE 5432