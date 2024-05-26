CREATE TABLE IF NOT EXISTS Client (
    id SERIAL PRIMARY KEY,
    Email VARCHAR(50) NOT NULL,
    Password VARCHAR(50) NOT NULL,
    Silver INT NOT NULL,
    Gold INT NOT NULL,
    General_experience INT NOT NULL,
    Banned BOOLEAN
);