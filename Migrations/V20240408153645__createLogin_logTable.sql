-- Create Login_log table
CREATE TABLE IF NOT EXISTS Login_log (
    id SERIAL PRIMARY KEY,
    Time DATE NOT NULL,
    IP VARCHAR(50) NOT NULL,
    Device_type VARCHAR(10) NOT NULL
);
