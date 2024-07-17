-- Create DATABASE
CREATE DATABASE cc_db;

-- Connect to new database
\c cc_db

-- Create User for DB
CREATE USER cc_admin WITH PASSWORD 'toortoor';

-- Grant Privileges
GRANT ALL PRIVILEGES ON DATABASE cc_db TO cc_admin;

-- Execute Schema script.
