FROM mysql

COPY ./db_info/db_schema.sql /tmp
COPY notebooks/tables_creation/final_tables/ ./final_tables/

CMD ["mysqld", "--init-file=/tmp/db_schema.sql", "--secure-file-priv=./final_tables/"]

