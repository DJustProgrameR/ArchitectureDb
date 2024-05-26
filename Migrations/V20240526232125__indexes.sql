CREATE INDEX IF NOT EXISTS idx_Client_Replay ON Client_Replay (Replay_ID, Client_ID);
CREATE INDEX IF NOT EXISTS idx_Tank_status ON Tank_status (Tank_ID, Client_ID);