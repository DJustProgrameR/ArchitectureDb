-- Create Moderator table
CREATE TABLE IF NOT EXISTS Moderator (
    id SERIAL PRIMARY KEY,
    Email VARCHAR(50) NOT NULL,
    Password VARCHAR(50) NOT NULL
);
