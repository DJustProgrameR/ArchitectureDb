-- Create Gun_Turret_Tank table
CREATE TABLE IF NOT EXISTS Gun_Turret_Tank (
    Gun_ID INT NOT NULL,
    Tank_ID INT NOT NULL,
    Turret_ID INT NOT NULL,
    Angle_up INTEGER[] NOT NULL,
    Angle_down INTEGER[] NOT NULL,
    PRIMARY KEY (Gun_ID, Tank_ID, Turret_ID),
    FOREIGN KEY (Gun_ID) REFERENCES Gun(id),
    FOREIGN KEY (Tank_ID) REFERENCES Tank(id),
    FOREIGN KEY (Turret_ID) REFERENCES Turret(id)
);
