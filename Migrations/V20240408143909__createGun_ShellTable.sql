-- Create Gun_Shell table
CREATE TABLE IF NOT EXISTS Gun_Shell (
    Gun_ID INT NOT NULL,
    Shell_ID INT NOT NULL,
    PRIMARY KEY (Gun_ID, Shell_ID),
    FOREIGN KEY (Gun_ID) REFERENCES Gun(id),
    FOREIGN KEY (Shell_ID) REFERENCES Shell(id)
);
