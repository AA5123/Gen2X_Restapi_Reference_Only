**Description:**
Disables the TagFocus feature, returning tags to normal operational mode where all tags respond to every inventory round regardless of prior reads.

**Usage:**
Send this command to deactivate TagFocus on the reader. Once disabled, all tags will respond to every inventory round, even if they were previously read in the current session. This is useful when you need to track tag movement, verify tag presence continuously, or when inventory redundancy is more important than throughput optimization.

**Parameters (MQTT & REST):**

- **enabled** (boolean): Disable TagFocus feature Must be `False`.

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