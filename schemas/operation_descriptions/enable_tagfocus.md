**Description:**
Enables TagFocus feature so tags that have already been inventoried remain silent in subsequent inventory rounds, allowing the reader to focus exclusively on new or unread tags.

**Usage:**
Send this command to activate TagFocus on the reader. Once enabled, any tag that has been successfully read in the current session (S1) will stop responding to subsequent inventory rounds. This dramatically improves read rates in dense tag environments by eliminating duplicate reads and concentrating RF energy on newly encountered tags.

**Parameters (MQTT & REST):**

- **enabled** (boolean): Enable TagFocus feature Must be `True`.

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