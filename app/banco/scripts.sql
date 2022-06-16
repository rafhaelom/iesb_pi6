--- Criação do banco de dados ---
CREATE DATABASE saude_sus
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;

--- Criação de schema ---
CREATE SCHEMA "sih-sus"
    AUTHORIZATION postgres;

