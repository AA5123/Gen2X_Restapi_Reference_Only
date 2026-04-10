**Description:**
Enable Inventory of Protected Tags — Grants the reader authorization to inventory protected tags using the correct 32-bit access password.

**Usage:**
Send this command with the 32-bit access password. The reader will use this password to authenticate and unmask all protected tags that match during inventory rounds. This allows the reader to interact with protected tags without permanently removing their Protected Mode.

**Persistence:** The authorization remains active across stop/start cycles as long as the MQTT session stays connected. A reader reboot or MQTT disconnect clears the authorization, and you must re-send this command to restore visibility.

**Parameters:**
- `action` (string): Set to `enableTagVisibility` to allow inventory of protected tags
- `password` (string): A 32-bit (8-character hexadecimal) access password for authentication
