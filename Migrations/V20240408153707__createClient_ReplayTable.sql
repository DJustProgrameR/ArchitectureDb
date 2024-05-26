-- Create Client_Replay table
CREATE TABLE IF NOT EXISTS Client_Replay (
    Replay_ID INT NOT NULL,
    Client_ID INT NOT NULL,
    PRIMARY KEY (Replay_ID, Client_ID),
    FOREIGN KEY (Replay_ID) REFERENCES Replay(id),
    FOREIGN KEY (Client_ID) REFERENCES Client(id)
);
