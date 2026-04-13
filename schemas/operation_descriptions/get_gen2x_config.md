**Description:**
Retrieves and displays the current Gen2X configuration stored on the reader, including all enabled features and their settings.

**Usage:**
Send this command with an empty payload to query the reader's current Gen2X configuration state. The response will contain all previously configured settings such as TagProtect states, FastID status, TagFocus status, Tag Quieting lists, and other Gen2X features. Use this command to verify your configuration before starting the reader or to audit the current settings. If no Gen2X configuration has been set, the response returns an empty configuration object.

---

---

---

<div style="background:#e0f7fa;padding:6px 12px;font-weight:600;border-radius:4px;color:#006064;margin-bottom:4px;">MQTT Endpoint Details</div>

| Field | Value |
|-------|-------|
| Command | `get_impinjGen2X` |

<div style="background:#e8eaf6;padding:6px 12px;font-weight:600;border-radius:4px;color:#1a237e;margin-bottom:4px;">REST Endpoint Details</div>

| Field | Value |
|-------|-------|
| Method | <span style="display:inline-block;background:#ffd54f;color:#795548;font-weight:700;padding:2px 10px;border-radius:12px;margin-right:8px;">GET</span>`GET` |
| Path | `/cloud/impinjGen2X` |
| OperationId | `getImpinjGen2X` |
| Content-Type | `application/json` |

> Returns the current Gen2X configuration as last saved. Returns an empty object if no configuration has been set.

**Parameters (MQTT & REST)**

_The following parameters apply to both MQTT and REST unless otherwise noted._

_No parameters required._
