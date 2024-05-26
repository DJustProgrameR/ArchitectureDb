-- Create Gun_equip_status table
CREATE TABLE IF NOT EXISTS Gun_equip_status (
    Gun_ID INT NOT NULL,
    Client_ID INT NOT NULL,
    Tank_ID INT NOT NULL,
    Status INT NOT NULL,
    Table_position INT NOT NULL,
    Table_prev_position INT,
    PRIMARY KEY (Gun_ID, Client_ID, Tank_ID),
    FOREIGN KEY (Gun_ID) REFERENCES Gun(id),
    FOREIGN KEY (Client_ID) REFERENCES Client(id),
    FOREIGN KEY (Tank_ID) REFERENCES Tank(id)
);
