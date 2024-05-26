-- Create Moderator_Replay table
CREATE TABLE IF NOT EXISTS Moderator_Replay (
    Moderator_ID INT NOT NULL,
    Replay_ID INT NOT NULL,
    PRIMARY KEY (Moderator_ID, Replay_ID),
    FOREIGN KEY (Moderator_ID) REFERENCES Moderator(id),
    FOREIGN KEY (Replay_ID) REFERENCES Replay(id)
);
