-- Create Shell table
CREATE TABLE IF NOT EXISTS Shell (
    id SERIAL PRIMARY KEY,
    Price INT NOT NULL,
    Penetration INT NOT NULL,
    Shell_type VARCHAR(10) NOT NULL,
    Max_ricochet_angle INT NOT NULL,
    Image_filepath VARCHAR(256) NOT NULL
);
