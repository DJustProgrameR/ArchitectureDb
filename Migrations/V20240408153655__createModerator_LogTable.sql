-- Create Moderator_Log table
CREATE TABLE IF NOT EXISTS Moderator_Log (
    Moderator_ID INT NOT NULL,
    Login_ID INT NOT NULL,
    PRIMARY KEY (Moderator_ID, Login_ID),
    FOREIGN KEY (Moderator_ID) REFERENCES Moderator(id),
    FOREIGN KEY (Login_ID) REFERENCES Login_log(id)
);
