FROM postgres:latest

# Set environment variables
ENV POSTGRES_DB=EIE
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword
ENV max_wal_size='10GB'

# Create a directory to store SQL scripts and CSV files
WORKDIR /usr/src/app

# Copy SQL scripts and CSV files
COPY ./db_info/db_schema.sql .
COPY ./notebooks/tables_creation/final_tables/ final_tables/

# Run SQL scripts during container initialization
COPY ./db_info/db_schema.sql /docker-entrypoint-initdb.d/

# Expose PostgreSQL default port
EXPOSE 5432