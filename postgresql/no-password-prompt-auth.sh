#!/bin/bash
source ../.env
export PGPASSWORD="$POSTGRES_PASSWORD"
psql -h $POSTGRES_HOST -U $POSTGRES_USER --no-password -p $POSTGRES_PORT -d $POSTGRES_DB -f a01.sql;