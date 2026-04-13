**Description:**
Retrieves and displays the current Gen2X configuration stored on the reader, including all enabled features and their settings.

**Usage:**
Send this command with an empty payload to query the reader's current Gen2X configuration state. The response will contain all previously configured settings such as TagProtect states, FastID status, TagFocus status, Tag Quieting lists, and other Gen2X features. Use this command to verify your configuration before starting the reader or to audit the current settings. If no Gen2X configuration has been set, the response returns an empty configuration object.

---

---

**MQTT Endpoint Details**

| Field | Value |
|-------|-------|
| Publish Topic | `controlrequest` |
| Subscribe Topic | `controlresponse` |
| Command | `get_impinjGen2X` |

**MQTT Parameters**

_No parameters required._

---

**REST Endpoint Details**

| Field | Value |
|-------|-------|
| Method | `GET` |
| Path | `/cloud/impinjGen2X` |
| OperationId | `getImpinjGen2X` |
| Content-Type | `application/json` |

> Returns the current Gen2X configuration as last saved. Returns an empty object if no configuration has been set.

**REST Parameters**

_No parameters required._
