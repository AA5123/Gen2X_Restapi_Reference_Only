**Description:**
Enable Impinj Protected Mode with Short Range — Protects an RFID tag with a 32-bit access password and restricts its response range to short distance only.

**Usage:**
Send this command with the target tag's EPC ID, a 32-bit access password, and set `enableShortRange` to `true`. The tag enters Protected Mode and only responds to readers in close physical proximity. This is ideal for point-of-sale operations or scenarios requiring location-specific tag reads.

**Parameters (MQTT & REST):**

- **action** (string): Enables Protected Mode on the tag Must be `enableTagProtection`.
- **password** (string): 8-character hexadecimal 32-bit password
- **tagID** (string): Hexadecimal tagID (EPC) of the target tag
- **enableShortRange** (boolean): true to enable short-range protection mode for higher security

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