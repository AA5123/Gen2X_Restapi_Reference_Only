**Description:**
Retrieves and displays the current Gen2X configuration stored on the reader, including all enabled features and their settings.

**Usage:**
Send this command with an empty payload to query the reader's current Gen2X configuration state. The response will contain all previously configured settings such as TagProtect states, FastID status, TagFocus status, Tag Quieting lists, and other Gen2X features. Use this command to verify your configuration before starting the reader or to audit the current settings. If no Gen2X configuration has been set, the response returns an empty configuration object.

**Parameters (MQTT & REST):**

_No parameters required._

### MQTT Endpoint Details

| Field | Value |
| --- | --- |
| Command | `get_impinjGen2X` |

### REST Endpoint Details

| Field | Value |
| --- | --- |
| Method | `GET` |
| Path | `/cloud/impinjGen2X` |
| Content-Type | `application/json` |