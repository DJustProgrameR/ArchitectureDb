-- Create Tank table
CREATE TABLE IF NOT EXISTS Tank (
    id SERIAL PRIMARY KEY,
    Level INT NOT NULL,
    Mass INT NOT NULL,
    Power INT NOT NULL,
    Ratio INT NOT NULL,
    Max_load INT NOT NULL,
    "3D_model_filepath" VARCHAR(256) NOT NULL,
    Purchase_price INT NOT NULL,
    Research_price INT NOT NULL,
    "Image_filepath" VARCHAR(256) NOT NULL,
    Table_position INT NOT NULL,
    Table_next_position INT
);
