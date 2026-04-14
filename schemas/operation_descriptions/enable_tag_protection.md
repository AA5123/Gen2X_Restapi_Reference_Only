**Description:**
Enable Impinj Protected Mode — Locks an RFID tag using a 32-bit access password, rendering it invisible to readers.

**Usage:**
Send this command with the target tag's EPC ID and a 32-bit access password. Once enabled, the tag enters Protected Mode and ceases to respond to standard inventory commands. The tag remains RF silent and inaccessible until a reader provides the correct password.

**Parameters (MQTT & REST):**

- **action** (string): Enables Protected Mode on the tag Must be `enableTagProtection`.
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