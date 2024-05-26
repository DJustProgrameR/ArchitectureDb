CREATE TABLE  IF NOT EXISTS Turret_equip_status (
    Turret_ID INT NOT NULL,
    Client_ID INT NOT NULL,
    Tank_ID INT NOT NULL,
    Status INT NOT NULL,
    Table_position INT NOT NULL,
    Table_prev_position INT,
    PRIMARY KEY (Turret_ID, Client_ID, Tank_ID),
    FOREIGN KEY (Turret_ID) REFERENCES Turret(id),
    FOREIGN KEY (Client_ID) REFERENCES Client(id),
    FOREIGN KEY (Tank_ID) REFERENCES Tank(id)
);