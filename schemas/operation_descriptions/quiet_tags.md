**Description:**
Selectively silences one or more specific tags by their EPC ID, preventing them from responding to inventory rounds without affecting other tags.

**Usage:**
Send this command with an array of one or more EPC IDs to quiet. Quieted tags will not participate in inventory responses and will not transmit RF signals to the reader. This is useful for isolating problematic tags, managing high-density inventory operations, or testing specific tag subsets. You can quiet up to 31 tag EPCs in a single command.

**Parameters (MQTT & REST):**

- **action** (string): Silence the specified tags Must be `quiet`.
- **tagIDs** (array): List of tag EPCs (hex strings) to quiet

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