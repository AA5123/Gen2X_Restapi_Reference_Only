**Description:**
Disables the FastID feature, returning tags to standard inventory mode where they return only the EPC (Electronic Product Code).

**Usage:**
Send this command to deactivate FastID on the reader. Once disabled, tags will only return their EPC in inventory responses. If you need the TID (Tag Identifier), you must perform a separate dedicated TID read operation. This is useful for reducing response payload size or simplifying data processing when TID data is not required.

**Parameters (MQTT & REST):**

- **enabled** (boolean): Disable FastID feature Must be `False`.

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