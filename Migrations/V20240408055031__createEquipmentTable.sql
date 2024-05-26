-- Create Equipment table
CREATE TABLE IF NOT EXISTS Equipment (
    id SERIAL PRIMARY KEY,
    Purchase_price INT NOT NULL,
    Equip_type VARCHAR(10) NOT NULL
);
