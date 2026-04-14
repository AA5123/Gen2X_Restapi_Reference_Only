**Description:**
Stops the reader radio immediately, halting all inventory operations and RF transmissions.

**Usage:**
Send this command with an empty payload to stop the reader radio. You must stop the radio before applying any Gen2X configuration changes such as enabling/disabling Protected Mode, FastID, TagFocus, or Tag Quieting. Always wait for the success response before attempting to configure settings or restart the radio. Stopping the reader is mandatory for synchronized configuration management.

**Parameters (MQTT & REST):**

_No parameters required._

### MQTT Endpoint Details

| Field | Value |
| --- | --- |
| Command | `stop` |

### REST Endpoint Details

| Field | Value |
| --- | --- |
| Method | `PUT` |
| Path | `/cloud/stop` |
| Content-Type | `application/json` |