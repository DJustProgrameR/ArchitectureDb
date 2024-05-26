-- Create Crew table
CREATE TABLE IF NOT EXISTS Crew (
    id SERIAL PRIMARY KEY,
    Client_ID INT NOT NULL,
    Name VARCHAR(50) NOT NULL,
    Skill_ID_1 INT,
    Skill_ID_2 INT,
    Skill_ID_3 INT,
    Image_filepath VARCHAR(256) NOT NULL,
    Role_ID INT NOT NULL,
    FOREIGN KEY (Client_ID) REFERENCES Client(id),
    FOREIGN KEY (Skill_ID_1) REFERENCES Skill(id),
    FOREIGN KEY (Skill_ID_2) REFERENCES Skill(id),
    FOREIGN KEY (Skill_ID_3) REFERENCES Skill(id),
    FOREIGN KEY (Role_ID) REFERENCES Role(id)
);
