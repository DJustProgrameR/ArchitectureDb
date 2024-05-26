-- Create Map table
CREATE TABLE IF NOT EXISTS Map (
    id SERIAL PRIMARY KEY,
    Description TEXT,
    Min_level INTEGER,
    Max_level INTEGER,
    "3D_model_filepath" VARCHAR(256) NOT NULL
);
