-- Create Skill_Role table
CREATE TABLE IF NOT EXISTS Skill_Role (
    Role_ID INT NOT NULL,
    Skill_ID INT NOT NULL,
    PRIMARY KEY (Role_ID, Skill_ID),
    FOREIGN KEY (Role_ID) REFERENCES Role(id),
    FOREIGN KEY (Skill_ID) REFERENCES Skill(id)
);
