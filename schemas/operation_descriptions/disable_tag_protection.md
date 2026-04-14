**Description:**
Disable Impinj Protected Mode — Removes the 32-bit access password protection from an RFID tag, restoring normal operation.

**Usage:**
Send this command with the target tag's EPC ID and the 32-bit access password that was used to enable Protected Mode. Once disabled, the tag returns to normal operation and responds to all standard inventory commands without authentication.

**Parameters (MQTT & REST):**

- **action** (string): Disables Protected Mode on the tag Must be `disableTagProtection`.
- **password** (string): 8-character hexadecimal 32-bit password
- **tagID** (string): Tag EPC ID

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