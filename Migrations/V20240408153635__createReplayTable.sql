-- Create Replay table
CREATE TABLE IF NOT EXISTS Replay (
    id SERIAL PRIMARY KEY,
    Map_ID INT NOT NULL,
    Video_filepath VARCHAR(256),
    FOREIGN KEY (Map_ID) REFERENCES Map(id)
);
