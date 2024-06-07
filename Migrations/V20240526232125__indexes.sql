CREATE INDEX IF NOT EXISTS idx_Client_Replay ON Client_Replay (Replay_ID, Client_ID);
CREATE INDEX IF NOT EXISTS idx_Tank_status ON Tank_status (Tank_ID, Client_ID);
CREATE INDEX IF NOT EXISTS idx_Gun_equip_status ON Gun_equip_status (Gun_ID, Client_ID, Tank_ID);
CREATE INDEX IF NOT EXISTS idx_Turret_equip_status ON Turret_equip_status (Turret_ID, Client_ID, Tank_ID);