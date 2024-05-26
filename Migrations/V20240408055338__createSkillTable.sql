-- Create Skill table
CREATE TABLE IF NOT EXISTS Skill (
    id SERIAL PRIMARY KEY,
    Research_price INT NOT NULL,
    Description TEXT,
    Image_filepath VARCHAR(256) NOT NULL
);
