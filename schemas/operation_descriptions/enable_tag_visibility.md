**Description:**
Enable Inventory of Protected Tags — Grants the reader authorization to inventory protected tags using the correct 32-bit access password.

**Usage:**
Send this command with the 32-bit access password. The reader will use this password to authenticate and unmask all protected tags that match during inventory rounds. This allows the reader to interact with protected tags without permanently removing their Protected Mode.

**Parameters (MQTT & REST):**

- **action** (string): Enables the reader to read protected tags Must be `enableTagVisibility`.
- **password** (string): 8-character hexadecimal 32-bit password

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