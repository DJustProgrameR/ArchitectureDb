DROP TABLE  Tank_Status;
CREATE TABLE IF NOT EXISTS Tank_Status
(
    Tank_ID INT NOT NULL,
    Client_ID INT NOT NULL,
    Experience INT NOT NULL,
    Status INT NOT NULL,
    Shell_ID INT,
    Equiped_amount INT,
    Gun_ID INT NOT NULL,
    Turret_ID INT NOT NULL,
    Crew_ID_1 INT,
    Crew_ID_2 INT,
    Crew_ID_3 INT,
    Crew_ID_4 INT,
    Crew_ID_5 INT,
    Crew_ID_6 INT,
    Equip_ID_1 INT,
    Equip_ID_2 INT,
    Equip_ID_3 INT,
    PRIMARY KEY (Tank_ID, Client_ID),
    FOREIGN KEY (Tank_ID) REFERENCES Tank(id),
    FOREIGN KEY (Client_ID) REFERENCES Client(id),
    FOREIGN KEY (Shell_ID) REFERENCES Shell(id),
    FOREIGN KEY (Gun_ID) REFERENCES Gun(id),
    FOREIGN KEY (Turret_ID) REFERENCES Turret(id),
    FOREIGN KEY (Crew_ID_1) REFERENCES Crew(id),
    FOREIGN KEY (Crew_ID_2) REFERENCES Crew(id),
    FOREIGN KEY (Crew_ID_3) REFERENCES Crew(id),
    FOREIGN KEY (Crew_ID_4) REFERENCES Crew(id),
    FOREIGN KEY (Crew_ID_5) REFERENCES Crew(id),
    FOREIGN KEY (Crew_ID_6) REFERENCES Crew(id),
    FOREIGN KEY (Equip_ID_1) REFERENCES Equipment(id),
    FOREIGN KEY (Equip_ID_2) REFERENCES Equipment(id),
    FOREIGN KEY (Equip_ID_3) REFERENCES Equipment(id)
) PARTITION BY RANGE (Tank_ID);

CREATE TABLE IF NOT EXISTS TankPart1 PARTITION OF Tank_Status
    FOR VALUES FROM (0) TO (5);

CREATE TABLE IF NOT EXISTS TankPart2 PARTITION OF Tank_Status
    FOR VALUES FROM (5) TO (66);

CREATE TABLE IF NOT EXISTS TankPart3 PARTITION OF Tank_Status
    FOR VALUES FROM (66) TO (101);