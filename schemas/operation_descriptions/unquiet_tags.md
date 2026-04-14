**Description:**
Restores previously silenced tags, allowing them to resume normal participation in inventory rounds.

**Usage:**
Send this command with the EPC IDs of the tags you wish to restore. These must be the same EPC IDs you provided to the Quiet Tags command. Once sent, the specified tags will resume responding to inventory operations and will transmit RF signals normally. You can restore individual tags or multiple tags in a single command. Tags not explicitly restored remain in quiet state.

**Parameters (MQTT & REST):**

- **action** (string): Restore the specified tags Must be `unquiet`.
- **tagIDs** (array): List of tag EPCs (hex strings) to unquiet

### MQTT Endpoint Details

| Field | Value |
| --- | --- |
| Command | `set_impinjGen2X` |

### REST Endpoint Details

| Field | Value |
| --- | --- |
| Method | `PUT` |
| Path | `/cloud/impinjGen2X` |
| Content-Type | `application/json` |