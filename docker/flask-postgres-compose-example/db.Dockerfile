FROM postgres:latest
EXPOSE 5432
ENV POSTGRES_USER=example
ENV POSTGRES_PASSWORD=example
ENV POSTGRES_DB=example_db
ENV PGPASSWORD=example
COPY ./backend/setup.sql /docker-entrypoint-initdb.d/setup.sql
