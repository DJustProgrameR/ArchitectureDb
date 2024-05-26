-- Create Equipment_status table
CREATE TABLE IF NOT EXISTS Equipment_status (
    Equip_ID INT NOT NULL,
    Client_ID INT NOT NULL,
    Equiped_amount INT NOT NULL,
    General_amount INT NOT NULL,
    PRIMARY KEY (Equip_ID, Client_ID),
    FOREIGN KEY (Equip_ID) REFERENCES Equipment(id),
    FOREIGN KEY (Client_ID) REFERENCES Client(id)
);
