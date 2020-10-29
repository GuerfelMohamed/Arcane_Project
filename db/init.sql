CREATE DATABASE arcane;
use arcane;

CREATE TABLE cities (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    name VARCHAR(100)
);

CREATE TABLE types (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    name VARCHAR(100)
);

INSERT INTO cities
  (name)
VALUES
  ('paris'),
  ('lyon'),
  ('nice');

INSERT INTO types
  (name)
VALUES
  ('T1'),
  ('T2'),
  ('T3');