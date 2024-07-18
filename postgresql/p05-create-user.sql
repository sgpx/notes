create database foobar_db;
\c foobar_db
create user foobar_user with password 'foobar_pwd_123';
create table foobar_requests(request_id bigserial primary key, request_data jsonb, created_at timestamp);
grant all privileges on database foobar_db to foobar_user;
grant all privileges on foobar_requests to foobar_user;
grant all privileges on foobar_requests_request_id_seq to foobar_user;