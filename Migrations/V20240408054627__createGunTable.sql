CREATE TABLE IF NOT EXISTS Gun (
    id SERIAL PRIMARY KEY,
    Mass INT NOT NULL,
    "3D_model_filepath" VARCHAR(256) NOT NULL,
    Damage INT NOT NULL,
    Image_filepath VARCHAR(256) NOT NULL
);