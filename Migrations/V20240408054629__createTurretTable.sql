-- Create Turret table
CREATE TABLE IF NOT EXISTS Turret (
    id SERIAL PRIMARY KEY,
    Research_price INT NOT NULL,
    Purchase_price INT NOT NULL,
    Mass INT NOT NULL,
    "3D_model_filepath" VARCHAR(256) NOT NULL,
    Image_filepath VARCHAR(256) NOT NULL
);
