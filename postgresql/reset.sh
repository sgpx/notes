#!/bin/bash
./pg_ctl -D ~/pgdata stop
rm -rf ~/pgdata
mkdir ~/pgdata
./pg_ctl -D ~/pgdata init
./pg_ctl -D ~/pgdata start -l logfile
./createdb testdb
./createuser --superuser super1
psql -h localhost -U super1 testdb -f ~/cmd.psql
